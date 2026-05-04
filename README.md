<!-- altmetric-validator-ai/README.md -->

# 🛡️ Wunaraha: Framework Audit Halusinasi Metrik Alternatif

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Transformers-yellow)](https://huggingface.co/)
[![Tests](https://img.shields.io/badge/tests-12%20passed-green)]()
[![Coverage](https://img.shields.io/badge/coverage-74%25-blue)]()

> *"Apakah mereka benar-benar membaca abstraknya, atau hanya membaca judulnya?"*

**Wunaraha** adalah *framework* Python untuk mengaudit kualitas metrik alternatif (Altmetrics). Tools ini menggunakan AI dan NLP untuk **membedakan antara Buzz Viral (Kebisingan) vs. Intellectual Adoption (Adopsi Intelektual)** dalam percakapan media sosial tentang publikasi ilmiah.

### 🎯 Masalah
Metrik seperti H-index rentan terhadap *self-citation* dan *citation cartels*. Sebagai gantinya, muncul Altmetrics yang mengukur perhatian di media sosial. Namun, Altmetrics juga memiliki kelemahan serius:
- **Bot dan Manipulasi**: Download dan mention bisa dibeli atau diotomatisasi.
- **Hype Sesaat**: Sebuah makalah bisa viral karena judul kontroversial, bukan karena substansinya.
- **Kebisingan**: Tidak ada bedanya antara "Wow, ini keren!" dengan "Ini akan mengubah cara saya bekerja."

### 🤖 Solusi: Audit Berbasis AI

**Wunaraha** memanfaatkan **Large Language Models (LLMs)** dan **Natural Language Processing (NLP)** untuk mengaudit percakapan di balik metrik.

1.  **Koleksi Data**: Mengambil tweet/post/blog yang merujuk pada sebuah DOI.
2.  **Analisis Kedalaman (Depth Analysis)**: Menggunakan model Transformer (seperti **SciBERT** atau **RoBERTa**) untuk mengklasifikasikan teks ke dalam tiga kategori:
    - **🧠 Adopsi Intelektual**: Penulis menunjukkan pemahaman mendalam, mengaitkan dengan pekerjaan sendiri, atau mengkritisi metodologi.
    - **📢 Buzz/Hype**: Sekadar membagikan tautan, pujian kosong, atau reaksi emosional singkat.
    - **🤖 Bot/Spam**: Akun otomatis yang mem-posting tanpa konteks.
3.  **Skor "Altmetric Purity"**: Metrik baru yang kami usulkan, yaitu persentase mention yang termasuk kategori *Adopsi Intelektual*.

### 📦 Instalasi & Penggunaan Cepat

#### Instalasi Development (Recommended)
```bash
git clone https://github.com/stipwunaraha/altmetric-validator-ai.git
cd altmetric-validator-ai

# Instal semua dependencies untuk development dan testing
pip install -r requirements-dev.txt

# Atau instal sebagai package editable
pip install -e ".[all]"
```

#### Instalasi Minimal (Production)
```bash
pip install wunaraha
# atau
pip install -r requirements.txt
```

#### Verifikasi Instalasi
```bash
# Jalankan unit tests
pytest

# Lihat coverage report
pytest --cov=wunaraha --cov-report=term-missing
```

**Contoh Penggunaan:**
```python
from wunaraha import AltmetricAuditor

auditor = AltmetricAuditor(use_gpu=True)

# Audit sebuah DOI
report = auditor.audit(doi="10.1126/science.abc1234")

print(f"Total Mention: {report.total_mentions}")
print(f"Adopsi Intelektual: {report.intellectual_adoption} ({report.purity_score:.2%})")
print(f"Buzz: {report.buzz_mentions}")
print(f"Terindikasi Bot: {report.suspected_bots}")
```

### 🚀 Fitur Utama

| Fitur | Deskripsi | Status |
|-------|-----------|--------|
| **Depth Analysis** | Klasifikasi mention ke dalam kategori: Adopsi Intelektual, Buzz/Hype, Bot/Spam | ✅ Ready |
| **Bot Detection** | Deteksi akun otomatis berdasarkan pola posting dan konten | ✅ Ready |
| **Altmetric Purity Score** | Metrik baru: persentase mention berkualitas tinggi | ✅ Ready |
| **Multi-Platform Support** | Twitter/X, Mastodon, Blog (via RSS) | 🚧 In Progress |
| **Dashboard Visualisasi** | Streamlit dashboard untuk explorasi hasil audit | 🚧 Planned |
| **Batch Processing** | Audit multiple DOI sekaligus | 🚧 Planned |

### 🏗️ Arsitektur

```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│   Data Source   │────▶│  Wunaraha Core   │────▶│    Output       │
│                 │     │                  │     │                 │
│ • Twitter API   │     │ • Mention Collector│     │ • Audit Report  │
│ • Mastodon API  │     │ • Depth Classifier │     │ • Purity Score  │
│ • RSS Feeds     │     │ • Bot Detector    │     │ • JSON/CSV      │
│                 │     │ • Report Generator│     │                 │
└─────────────────┘     └──────────────────┘     └─────────────────┘
                              │
                              ▼
                    ┌──────────────────┐
                    │  AI Models       │
                    │                  │
                    │ • SciBERT        │
                    │ • RoBERTa        │
                    │ • DeBERTa (soon) │
                    └──────────────────┘
```

### 📂 Struktur Repository

```
wunaraha/
├── wunaraha/              # Package utama
│   ├── __init__.py        # Export public API
│   ├── models.py          # Data models (Mention, AuditReport, EngagementType)
│   └── auditor.py         # Core logic (AltmetricAuditor class)
├── tests/                 # Unit tests
│   ├── test_auditor.py    # Test suite untuk auditor
│   └── ...
├── requirements.txt       # Dependencies minimal
├── requirements-dev.txt   # Dependencies development lengkap
├── pyproject.toml         # Package configuration
├── setup.py               # Setup script
├── example_usage.py       # Contoh penggunaan
└── docs/                  # Dokumentasi (coming soon)
```

### 🧪 Testing & Development

Repository ini dilengkapi dengan:
- **Unit Tests**: 12 test cases dengan 74% code coverage
- **Development Tools**: pytest, black, flake8, mypy, isort
- **CI/CD Ready**: Konfigurasi untuk automated testing

Lihat [SETUP_DEV.md](SETUP_DEV.md) untuk panduan lengkap setup development environment.

### 🚧 Roadmap
- [ ] Integrasi Twitter API v2 dan Mastodon API.
- [ ] Model klasifikasi *depth-of-engagement* berbasis **DeBERTa**.
- [ ] Dashboard Streamlit untuk visualisasi hasil audit.
- [ ] Dukungan untuk menganalisis berita dari Google News RSS.

### 📚 Referensi
- *Quantitative Methods in Research Evaluation Citation Indicators, Altmetrics, and Artificial Intelligence* (Thelwall, 2024).
- *Have we reached the limits of altmetrics?* (Research Information, 2023).

### 🤝 Kontribusi

Kami mencari *data scientist*, *NLP engineer*, dan peneliti yang tertarik dengan *research integrity*. 

**Cara Berkontribusi:**
1. Fork repository ini
2. Buat branch fitur (`git checkout -b feature/AmazingFeature`)
3. Commit perubahan (`git commit -m 'Add AmazingFeature'`)
4. Push ke branch (`git push origin feature/AmazingFeature`)
5. Buka Pull Request

**Development Setup:**
```bash
# Clone fork Anda
git clone https://github.com/YOUR_USERNAME/altmetric-validator-ai.git
cd altmetric-validator-ai

# Instal dependencies development
pip install -r requirements-dev.txt

# Jalankan tests sebelum commit
pytest --cov=wunaraha

# Format code
black wunaraha tests
isort wunaraha tests
```

Lihat [CONTRIBUTING.md](CONTRIBUTING.md) untuk panduan lengkap.

### 📄 Lisensi

MIT License - lihat [LICENSE](LICENSE) untuk detail.
