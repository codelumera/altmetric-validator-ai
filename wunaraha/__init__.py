"""
Wunaraha: Framework Audit Halusinasi Metrik Alternatif

Tools untuk membuktikan bahwa metrik alternatif (Altmetrics) juga rentan 
terhadap manipulasi bot dan hype cycle menggunakan AI.
"""

__version__ = "0.1.0"
__author__ = "Wunaraha Team"

from .auditor import AltmetricAuditor
from .models import Mention, AuditReport, EngagementType

__all__ = ["AltmetricAuditor", "Mention", "AuditReport", "EngagementType"]
