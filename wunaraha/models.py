"""
Data classes untuk hasil audit Altmetric.
"""

from dataclasses import dataclass, field
from typing import List, Dict, Optional


@dataclass
class Mention:
    """Representasi satu mention/tweet/post tentang sebuah DOI."""
    text: str
    source: str  # 'twitter', 'mastodon', 'blog', 'news'
    author: str
    timestamp: str
    url: str
    classification: str = "unknown"  # 'intellectual', 'buzz', 'bot'
    confidence: float = 0.0
    engagement_score: float = 0.0  # Likes + retweets + replies (normalized)


@dataclass
class AuditReport:
    """Laporan hasil audit untuk sebuah DOI."""
    doi: str
    total_mentions: int = 0
    
    # Klasifikasi
    intellectual_adoption: int = 0
    buzz_mentions: int = 0
    suspected_bots: int = 0
    unknown: int = 0
    
    # Skor
    purity_score: float = 0.0  # Persentase adopsi intelektual
    
    # Detail mentions
    mentions: List[Mention] = field(default_factory=list)
    
    # Metadata
    analysis_date: str = ""
    model_used: str = ""
    
    def calculate_purity_score(self):
        """Hitung skor Altmetric Purity."""
        if self.total_mentions == 0:
            self.purity_score = 0.0
        else:
            self.purity_score = self.intellectual_adoption / self.total_mentions
    
    def summary(self) -> str:
        """Ringkasan hasil audit."""
        return f"""
=== Laporan Audit Wunaraha ===
DOI: {self.doi}
Total Mention: {self.total_mentions}

Klasifikasi:
  🧠 Adopsi Intelektual: {self.intellectual_adoption} ({self.purity_score:.2%})
  📢 Buzz/Hype: {self.buzz_mentions}
  🤖 Terindikasi Bot: {self.suspected_bots}
  ❓ Tidak Diketahui: {self.unknown}

Skor Altmetric Purity: {self.purity_score:.2%}
Model yang digunakan: {self.model_used}
Tanggal Analisis: {self.analysis_date}
===============================
"""
