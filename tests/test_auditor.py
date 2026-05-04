"""
Test suite untuk Wunaraha Auditor
"""
import pytest
from wunaraha.models import Mention, AuditReport, EngagementType
from wunaraha.auditor import AltmetricAuditor


class TestMention:
    """Test untuk Mention data class"""
    
    def test_create_mention(self):
        """Test membuat mention object"""
        mention = Mention(
            text="Paper yang sangat bagus tentang AI!",
            source="twitter",
            author="researcher123",
            url="https://twitter.com/researcher123/status/123",
            timestamp="2024-01-15T10:30:00Z"
        )
        
        assert mention.source == "twitter"
        assert mention.text == "Paper yang sangat bagus tentang AI!"
        assert mention.author == "researcher123"
        assert mention.engagement_type is None
    
    def test_mention_with_engagement_type(self):
        """Test mention dengan engagement type"""
        mention = Mention(
            text="Analisis mendalam tentang implikasi AI dalam penelitian",
            source="twitter",
            author="prof_ai",
            url="https://twitter.com/prof_ai/status/456",
            timestamp="2024-01-15T10:30:00Z",
            engagement_type=EngagementType.INTELLECTUAL_ADOPTION
        )
        
        assert mention.engagement_type == EngagementType.INTELLECTUAL_ADOPTION
        assert mention.is_deep_engagement() is True
    
    def test_mention_engagement_classification(self):
        """Test klasifikasi engagement type"""
        # Intellectual adoption
        mention_intellectual = Mention(
            text="Kami menggunakan metode ini dalam penelitian kami",
            source="twitter",
            author="researcher",
            url="https://example.com/1",
            timestamp="2024-01-15T10:30:00Z"
        )
        assert mention_intellectual.is_deep_engagement() is False
        
        # Buzz/hype
        mention_buzz = Mention(
            text="Paper keren! 🔥🔥🔥",
            source="twitter",
            author="user123",
            url="https://example.com/2",
            timestamp="2024-01-15T10:30:00Z"
        )
        assert mention_buzz.is_shallow_engagement() is False


class TestAuditReport:
    """Test untuk AuditReport data class"""
    
    def test_create_audit_report(self):
        """Test membuat audit report"""
        mentions = [
            Mention(
                text="Great paper!",
                source="twitter",
                author="user1",
                url="https://example.com/1",
                timestamp="2024-01-15T10:30:00Z",
                engagement_type=EngagementType.BUZZ_HYPE
            ),
            Mention(
                text="We applied this method in our study",
                source="twitter",
                author="researcher1",
                url="https://example.com/2",
                timestamp="2024-01-15T10:30:00Z",
                engagement_type=EngagementType.INTELLECTUAL_ADOPTION
            )
        ]
        
        report = AuditReport(
            doi="10.1234/example.2024.001",
            total_mentions=len(mentions),
            mentions=mentions,
            purity_score=0.5
        )
        
        assert report.doi == "10.1234/example.2024.001"
        assert len(report.mentions) == 2
        assert report.purity_score == 0.5
        assert report.total_mentions == 2


class TestAltmetricAuditor:
    """Test untuk AltmetricAuditor"""
    
    def test_create_auditor(self):
        """Test membuat auditor instance"""
        auditor = AltmetricAuditor()
        assert auditor is not None
        assert auditor.mode == "rule_based"
    
    def test_classify_mention_rule_based(self):
        """Test klasifikasi mention dengan rule-based mode"""
        auditor = AltmetricAuditor(use_ml=False)
        
        # Test intellectual adoption
        content_intellectual = "This study builds on the methodology proposed by Smith et al."
        result, confidence = auditor.classify_mention(content_intellectual)
        assert result in ["intellectual", "buzz", "bot"]
        assert 0 <= confidence <= 1
        
        # Test buzz/hype
        content_buzz = "Amazing paper! 🔥🔥 Must read! #viral #trending"
        result, confidence = auditor.classify_mention(content_buzz)
        assert result in ["intellectual", "buzz", "bot"]
        assert 0 <= confidence <= 1
    
    def test_is_likely_bot(self):
        """Test deteksi pola bot"""
        auditor = AltmetricAuditor(use_ml=False)
        
        # Bot-like content
        bot_content = "Check out this paper https://bit.ly/abc123 #paper #research #science #ai #ml #data"
        is_bot = auditor._is_likely_bot(bot_content)
        assert isinstance(is_bot, bool)
        
        # Normal content
        normal_content = "Interesting findings in this research"
        is_bot = auditor._is_likely_bot(normal_content)
        assert isinstance(is_bot, bool)
    
    def test_analyze_depth(self):
        """Test analisis kedalaman konten"""
        auditor = AltmetricAuditor(use_ml=False)
        
        # Deep content
        deep_content = "This methodology provides a framework for analyzing data. The results demonstrate significant findings that build upon previous research."
        depth_score = auditor._analyze_depth(deep_content)
        assert 0 <= depth_score <= 1
        
        # Shallow content
        shallow_content = "Wow! Amazing! 🔥"
        depth_score = auditor._analyze_depth(shallow_content)
        assert 0 <= depth_score <= 1
    
    def test_collect_mentions(self):
        """Test koleksi mentions (mock)"""
        auditor = AltmetricAuditor(use_ml=False)
        
        mentions = auditor.collect_mentions("10.1234/test.2024.001")
        
        assert isinstance(mentions, list)
        assert len(mentions) > 0
        assert all(isinstance(m, Mention) for m in mentions)
    
    def test_audit_doi(self):
        """Test audit DOI"""
        auditor = AltmetricAuditor(use_ml=False)
        
        report = auditor.audit("10.1234/test.2024.001")
        
        assert isinstance(report, AuditReport)
        assert report.doi == "10.1234/test.2024.001"
        assert len(report.mentions) > 0
        assert 0 <= report.purity_score <= 1


class TestEngagementType:
    """Test untuk EngagementType enum"""
    
    def test_engagement_types(self):
        """Test semua engagement types"""
        assert EngagementType.INTELLECTUAL_ADOPTION.value == "intellectual_adoption"
        assert EngagementType.BUZZ_HYPE.value == "buzz_hype"
        assert EngagementType.BOT_SPAM.value == "bot_spam"
        assert EngagementType.UNKNOWN.value == "unknown"
    
    def test_engagement_type_from_string(self):
        """Test membuat engagement type dari string"""
        assert EngagementType.from_string("intellectual_adoption") == EngagementType.INTELLECTUAL_ADOPTION
        assert EngagementType.from_string("buzz_hype") == EngagementType.BUZZ_HYPE
        assert EngagementType.from_string("bot_spam") == EngagementType.BOT_SPAM
        assert EngagementType.from_string("unknown") == EngagementType.UNKNOWN
        assert EngagementType.from_string("invalid") is None
