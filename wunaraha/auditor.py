"""
Main auditor module untuk analisis Altmetric menggunakan AI.
"""

import re
from datetime import datetime
from typing import List, Dict, Optional, Tuple

try:
    from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification
    TRANSFORMERS_AVAILABLE = True
except ImportError:
    TRANSFORMERS_AVAILABLE = False

from .models import AuditReport, Mention


class AltmetricAuditor:
    """
    Auditor untuk menganalisis mention Altmetric dan membedakan antara:
    - Adopsi Intelektual (deep engagement)
    - Buzz/Hype (shallow engagement)
    - Bot/Spam (automated posting)
    """
    
    def __init__(self, use_gpu: bool = False, model_name: str = None, use_ml: bool = False):
        """
        Inisialisasi auditor dengan model klasifikasi.
        
        Args:
            use_gpu: Gunakan GPU jika tersedia
            model_name: Nama model HuggingFace untuk klasifikasi
            use_ml: Gunakan model ML (default False untuk mode rule-based ringan)
        """
        self.use_gpu = use_gpu and self._check_gpu_available()
        self.model_name = model_name or "cardiffnlp/twitter-roberta-base-sentiment"
        self.use_ml = use_ml
        self.classifier = None
        
        if self.use_ml and TRANSFORMERS_AVAILABLE:
            self._load_model()
        elif self.use_ml and not TRANSFORMERS_AVAILABLE:
            print("⚠️  Warning: transformers library tidak terinstal. Menggunakan mode simulasi.")
        else:
            print("ℹ️  Menggunakan mode rule-based classification (ringan, tanpa download model)")
    
    def _check_gpu_available(self) -> bool:
        """Cek apakah GPU tersedia."""
        try:
            import torch
            return torch.cuda.is_available()
        except ImportError:
            return False
    
    def _load_model(self):
        """Load model klasifikasi dari HuggingFace."""
        try:
            device = 0 if self.use_gpu else -1
            self.classifier = pipeline(
                "sentiment-analysis",
                model=self.model_name,
                device=device,
                truncation=True,
                max_length=512
            )
            print(f"✅ Model loaded: {self.model_name}")
        except Exception as e:
            print(f"⚠️  Gagal load model: {e}")
            print("Menggunakan mode fallback (rule-based classification)")
    
    def classify_mention(self, text: str) -> Tuple[str, float]:
        """
        Klasifikasikan sebuah mention ke dalam kategori:
        - 'intellectual': Adopsi intelektual (deep engagement)
        - 'buzz': Buzz/hype (shallow engagement)
        - 'bot': Terindikasi bot/spam
        
        Args:
            text: Teks mention/tweet/post
            
        Returns:
            Tuple (classification, confidence_score)
        """
        # Deteksi bot sederhana
        if self._is_likely_bot(text):
            return "bot", 0.85
        
        # Analisis kedalaman konten
        depth_score = self._analyze_depth(text)
        
        if depth_score > 0.7:
            return "intellectual", depth_score
        elif depth_score < 0.3:
            return "buzz", 1.0 - depth_score
        else:
            # Gunakan model ML jika tersedia
            if self.classifier:
                try:
                    result = self.classifier(text[:512])[0]
                    label = result['label']
                    score = result['score']
                    
                    # Mapping label ke kategori kita
                    if 'positive' in label.lower() and score > 0.6:
                        # Cek lagi apakah ini buzz atau intellectual
                        if self._contains_deep_engagement(text):
                            return "intellectual", score
                        else:
                            return "buzz", score
                    else:
                        return "buzz", score
                except Exception:
                    pass
            
            # Fallback: rule-based
            if depth_score > 0.5:
                return "intellectual", depth_score
            else:
                return "buzz", 1.0 - depth_score
    
    def _is_likely_bot(self, text: str) -> bool:
        """Deteksi apakah teks kemungkinan dari bot."""
        # Bot biasanya: banyak hashtag, banyak URL, teks sangat pendek/panjang
        url_count = len(re.findall(r'http[s]?://\S+', text))
        hashtag_count = len(re.findall(r'#\w+', text))
        mention_count = len(re.findall(r'@\w+', text))
        
        # Teks terlalu pendek tanpa konteks
        if len(text.split()) < 5 and (url_count >= 1 or hashtag_count >= 3):
            return True
        
        # Terlalu banyak hashtag/mention
        if hashtag_count > 5 or mention_count > 3:
            return True
        
        # Repetisi karakter
        if re.search(r'(.)\1{4,}', text):
            return True
        
        return False
    
    def _analyze_depth(self, text: str) -> float:
        """
        Analisis kedalaman engagement berdasarkan fitur linguistik.
        Returns score 0-1 (1 = sangat dalam/intelektual)
        """
        score = 0.5  # Base score
        
        words = text.lower().split()
        word_count = len(words)
        
        # Indikator adopsi intelektual
        intellectual_indicators = [
            'method', 'methodology', 'approach', 'framework', 'model',
            'result', 'finding', 'conclusion', 'evidence', 'data',
            'analysis', 'study', 'research', 'experiment', 'theory',
            'compare', 'contrast', 'critique', 'limitation', 'future work',
            'implement', 'apply', 'extend', 'build upon', 'based on',
            'agree', 'disagree', 'however', 'therefore', 'because',
            'suggest', 'propose', 'demonstrate', 'show', 'prove'
        ]
        
        # Indikator buzz/hype
        buzz_indicators = [
            'wow', 'amazing', 'awesome', 'great', 'cool', 'nice',
            'check out', 'look at', 'must read', 'breaking', 'new',
            '🔥', '💯', '👏', '😍', '🚀', '!!!', '...'
        ]
        
        # Hitung skor berdasarkan indikator
        intel_count = sum(1 for word in words if any(ind in word for ind in intellectual_indicators))
        buzz_count = sum(1 for word in words if any(ind in word for ind in buzz_indicators))
        
        # Adjust score
        if intel_count > 0:
            score += min(0.3, intel_count * 0.05)
        
        if buzz_count > 0:
            score -= min(0.3, buzz_count * 0.05)
        
        # Panjang teks (teks lebih panjang cenderung lebih mendalam)
        if word_count > 30:
            score += 0.1
        elif word_count < 10:
            score -= 0.1
        
        # Ada kutipan atau referensi
        if '"' in text or "'" in text or 'cite' in text.lower():
            score += 0.1
        
        # Normalize ke 0-1
        return max(0.0, min(1.0, score))
    
    def _contains_deep_engagement(self, text: str) -> bool:
        """Cek apakah teks mengandung engagement yang mendalam."""
        # Pola yang menunjukkan pemahaman mendalam
        deep_patterns = [
            r'\b(this|these|our|my)\s+(work|study|research|paper|result)',
            r'\b(build|extend|improve|modify)\s+on\b',
            r'\b(compare|contrast)\s+(with|to)\b',
            r'\b(agree|disagree)\s+(with|that)\b',
            r'\b(method|approach|technique)\s+(is|was|are|were)',
            r'\b(limitation|weakness|strength)\s+(of|in)\b',
            r'\b(future|next)\s+(work|step|research)',
        ]
        
        for pattern in deep_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                return True
        
        return False
    
    def collect_mentions(self, doi: str) -> List[Mention]:
        """
        Kumpulkan mentions untuk sebuah DOI.
        
        NOTE: Ini adalah implementasi stub. Dalam produksi, ini akan:
        - Query Twitter API v2
        - Query Mastodon API
        - Scrape blog/news sites
        - Query Altmetric.com API
        
        Untuk demo, kami generate data simulasi.
        """
        # TODO: Implementasi actual API calls
        # Untuk sekarang, return data dummy untuk testing
        print(f"📡 Mengumpulkan mentions untuk DOI: {doi}")
        
        # Simulasi beberapa mentions
        sample_mentions = [
            Mention(
                text="This paper presents a novel approach to metric validation. The methodology is sound and the results are compelling. Will definitely cite this in my future work.",
                source="twitter",
                author="@researcher_jane",
                timestamp="2024-01-15T10:30:00Z",
                url="https://twitter.com/researcher_jane/status/123",
                engagement_score=0.7
            ),
            Mention(
                text="Wow amazing paper! 🔥🔥🔥 Check it out! #research #science http://example.com/paper",
                source="twitter",
                author="@hype_bot_9000",
                timestamp="2024-01-15T11:00:00Z",
                url="https://twitter.com/hype_bot_9000/status/456",
                engagement_score=0.3
            ),
            Mention(
                text="We build upon their framework in our latest study. Their limitation analysis helped us identify gaps in the current literature. Strong contribution to the field.",
                source="blog",
                author="Dr. Smith's Research Blog",
                timestamp="2024-01-16T09:00:00Z",
                url="https://example-blog.com/post/123",
                engagement_score=0.9
            ),
            Mention(
                text="New paper alert! 🚀 Must read! 💯💯💯 #altmetrics #AI http://example.com/paper http://bit.ly/xyz",
                source="twitter",
                author="@auto_poster",
                timestamp="2024-01-15T12:00:00Z",
                url="https://twitter.com/auto_poster/status/789",
                engagement_score=0.2
            ),
        ]
        
        return sample_mentions
    
    def audit(self, doi: str, custom_mentions: List[Mention] = None) -> AuditReport:
        """
        Lakukan audit lengkap untuk sebuah DOI.
        
        Args:
            doi: Digital Object Identifier untuk diaudit
            custom_mentions: Optional list mentions custom (untuk testing)
            
        Returns:
            AuditReport dengan hasil lengkap
        """
        print(f"🔍 Memulai audit untuk DOI: {doi}")
        
        # Koleksi mentions
        if custom_mentions:
            mentions = custom_mentions
        else:
            mentions = self.collect_mentions(doi)
        
        # Inisialisasi report
        report = AuditReport(
            doi=doi,
            total_mentions=len(mentions),
            analysis_date=datetime.now().isoformat(),
            model_used=self.model_name
        )
        
        # Klasifikasi setiap mention
        for mention in mentions:
            classification, confidence = self.classify_mention(mention.text)
            mention.classification = classification
            mention.confidence = confidence
            
            # Update counter di report
            if classification == "intellectual":
                report.intellectual_adoption += 1
            elif classification == "buzz":
                report.buzz_mentions += 1
            elif classification == "bot":
                report.suspected_bots += 1
            else:
                report.unknown += 1
            
            report.mentions.append(mention)
        
        # Hitung purity score
        report.calculate_purity_score()
        
        print(report.summary())
        
        return report
