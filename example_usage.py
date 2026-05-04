"""
Contoh penggunaan Wunaraha - Altmetric Validator AI
"""

from wunaraha import AltmetricAuditor
from wunaraha.models import Mention


def main():
    # Inisialisasi auditor (gunakan use_ml=False untuk mode ringan tanpa download model)
    print("🚀 Inisialisasi Wunaraha Auditor...")
    auditor = AltmetricAuditor(use_gpu=False, use_ml=False)  # Set use_ml=True jika ingin pakai ML model
    
    # Contoh 1: Audit dengan data simulasi (default)
    print("\n" + "="*60)
    print("CONTOH 1: Audit DOI dengan data simulasi")
    print("="*60)
    
    report = auditor.audit(doi="10.1126/science.abc1234")
    
    print("\n📊 Detail Mentions:")
    for i, mention in enumerate(report.mentions, 1):
        print(f"\n{i}. [{mention.source}] {mention.author}")
        print(f"   Text: {mention.text[:100]}...")
        print(f"   Klasifikasi: {mention.classification.upper()}")
        print(f"   Confidence: {mention.confidence:.2%}")
    
    # Contoh 2: Audit dengan custom mentions
    print("\n" + "="*60)
    print("CONTOH 2: Audit dengan custom mentions")
    print("="*60)
    
    custom_mentions = [
        Mention(
            text="Their methodology extends previous work by incorporating multi-modal analysis. However, the sample size is limited. Future research should validate these findings with larger cohorts.",
            source="twitter",
            author="@prof_researcher",
            timestamp="2024-01-17T14:00:00Z",
            url="https://twitter.com/prof_researcher/status/999",
            engagement_score=0.8
        ),
        Mention(
            text="🔥🔥 NEW PAPER ALERT 🔥🔥 Check this out!!! #science #research #viral http://short.link/abc http://bit.ly/xyz #trending",
            source="twitter",
            author="@spam_bot_2024",
            timestamp="2024-01-17T14:30:00Z",
            url="https://twitter.com/spam_bot_2024/status/888",
            engagement_score=0.1
        ),
        Mention(
            text="We disagree with their conclusion about metric purity. The approach doesn't account for field-specific citation practices. Our study shows different results when controlling for discipline.",
            source="blog",
            author="Academic Critique Blog",
            timestamp="2024-01-18T10:00:00Z",
            url="https://academic-critique.org/post/456",
            engagement_score=0.95
        ),
        Mention(
            text="Nice paper 👏",
            source="twitter",
            author="@casual_reader",
            timestamp="2024-01-17T15:00:00Z",
            url="https://twitter.com/casual_reader/status/777",
            engagement_score=0.2
        ),
        Mention(
            text="This framework will be useful for our upcoming project on research evaluation. We plan to implement their scoring system and compare it with traditional citation metrics across different fields.",
            source="mastodon",
            author="@data_scientist@scholar.social",
            timestamp="2024-01-18T09:00:00Z",
            url="https://scholar.social/@data_scientist/123456",
            engagement_score=0.85
        ),
    ]
    
    report2 = auditor.audit(doi="10.1038/nature.xyz789", custom_mentions=custom_mentions)
    
    # Tampilkan perbandingan
    print("\n" + "="*60)
    print("RINGKASAN PERBANDINGAN")
    print("="*60)
    print(f"\nDOI 1: {report.doi}")
    print(f"  - Purity Score: {report.purity_score:.2%}")
    print(f"  - Intellectual: {report.intellectual_adoption}/{report.total_mentions}")
    
    print(f"\nDOI 2: {report2.doi}")
    print(f"  - Purity Score: {report2.purity_score:.2%}")
    print(f"  - Intellectual: {report2.intellectual_adoption}/{report2.total_mentions}")
    
    print("\n✅ Audit selesai!")
    print("\n💡 Tips: Skor Purity yang rendah (<30%) mengindikasikan banyak buzz/bot.")
    print("   Skor Purity yang tinggi (>60%) menunjukkan adopsi intelektual yang kuat.")


if __name__ == "__main__":
    main()
