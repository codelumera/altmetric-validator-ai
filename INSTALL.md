# 📦 Panduan Instalasi Wunaraha

Panduan lengkap untuk menginstal dan mengembangkan Wunaraha di localhost Anda.

## 🔧 Prasyarat

- Python 3.8 atau lebih baru
- pip (Python package manager)
- git (opsional, untuk clone repository)

## 🚀 Instalasi Cepat

### Opsi 1: Instalasi Development (Rekomendasi)

```bash
# Clone repository (jika belum)
git clone https://github.com/wunaraha/wunaraha.git
cd wunaraha

# Buat virtual environment (rekomendasi)
python -m venv venv

# Aktifkan virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate

# Instal dalam mode development
pip install -e ".[all]"
```

### Opsi 2: Instalasi dari requirements.txt

```bash
# Instal dependencies dasar
pip install -r requirements.txt

# Atau instal dengan semua dependencies opsional
pip install -r requirements.txt
pip install scikit-learn sentence-transformers  # ML features
pip install streamlit plotly  # Dashboard
pip install tweepy Mastodon.py python-dotenv  # API integrations
```

### Opsi 3: Instalasi Minimal

```bash
# Hanya dependencies core
pip install transformers torch pandas numpy requests
```

## 📁 Struktur Dependencies

### Core Dependencies (Wajib)
- `transformers>=4.30.0` - Model AI untuk klasifikasi
- `torch>=2.0.0` - Backend untuk model ML
- `pandas>=1.5.0` - Data processing
- `numpy>=1.24.0` - Numerical operations
- `requests>=2.28.0` - HTTP requests

### Optional Dependencies

#### Development Tools
```bash
pip install pytest pytest-cov black flake8 mypy isort pre-commit
```

#### Machine Learning Features
```bash
pip install scikit-learn sentence-transformers
```

#### Dashboard & Visualization
```bash
pip install streamlit plotly
```

#### API Integrations
```bash
pip install tweepy Mastodon.py python-dotenv
```

## 🧪 Menjalankan Tests

```bash
# Jalankan semua tests
pytest

# Jalankan dengan coverage report
pytest --cov=wunaraha --cov-report=html

# Buka coverage report
# Windows: start htmlcov/index.html
# Linux/Mac: open htmlcov/index.html
```

## 🔐 Konfigurasi Environment Variables

1. Salin template environment:
```bash
cp .env.example .env
```

2. Edit `.env` dan isi dengan kredensial API Anda (jika diperlukan)

## 💻 Mode Pengembangan

### Install dalam Mode Editable

```bash
# Ini memungkinkan Anda mengedit kode dan langsung melihat perubahan
pip install -e .
```

### Install dengan Extras

```bash
# Development tools saja
pip install -e ".[dev]"

# ML features saja
pip install -e ".[ml]"

# Dashboard saja
pip install -e ".[dashboard]"

# API integrations saja
pip install -e ".[api]"

# Semua dependencies
pip install -e ".[all]"
```

## 🎯 Verifikasi Instalasi

```python
# Test import
from wunaraha import AltmetricAuditor
from wunaraha.models import Mention, AuditReport

# Buat auditor instance
auditor = AltmetricAuditor()
print(f"Wunaraha version: {auditor.__class__.__module__}")
print("✅ Instalasi berhasil!")
```

## 🐛 Troubleshooting

### Error: ModuleNotFoundError

```bash
# Pastikan virtual environment aktif
# Instal ulang dependencies
pip install -e ".[all]"
```

### Error: torch tidak kompatibel

```bash
# Instal torch yang sesuai dengan sistem Anda
# Kunjungi: https://pytorch.org/get-started/locally/
pip install torch --index-url https://download.pytorch.org/whl/cu118  # Untuk CUDA 11.8
```

### Error: transformers versi lama

```bash
# Upgrade transformers
pip install --upgrade transformers
```

## 📝 Pre-commit Hooks (Opsional)

```bash
# Install pre-commit hooks
pre-commit install

# Jalankan manual
pre-commit run --all-files
```

## 🎨 Code Formatting

```bash
# Format code dengan Black
black wunaraha/ tests/

# Sort imports dengan isort
isort wunaraha/ tests/

# Lint dengan Flake8
flake8 wunaraha/ tests/
```

## 📊 Type Checking

```bash
# Jalankan mypy
mypy wunaraha/
```

## 🚀 Langkah Selanjutnya

Setelah instalasi:
1. Lihat `example_usage.py` untuk contoh penggunaan
2. Jalankan tests dengan `pytest`
3. Kembangkan fitur baru sesuai kebutuhan
4. Kontribusi kembali ke repository!

## 📞 Bantuan

Jika mengalami masalah:
- Cek [Issues](https://github.com/wunaraha/wunaraha/issues)
- Buat issue baru dengan detail error
- Dokumentasi lengkap di README.md
