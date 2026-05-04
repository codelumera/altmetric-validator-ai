# 🚀 Setup Development Environment - Wunaraha

Panduan lengkap untuk menyiapkan environment development dan testing di localhost.

## 📋 Prerequisites

- Python 3.8 atau lebih tinggi
- pip (Python package manager)
- git

## 🔧 Langkah Instalasi

### Opsi 1: Menggunakan requirements-dev.txt (RECOMMENDED)

Instal semua dependensi yang diperlukan untuk development dan testing:

```bash
# Install semua dependencies
pip install -r requirements-dev.txt
```

### Opsi 2: Menggunakan pyproject.toml

Instal package dalam mode development dengan semua dependencies:

```bash
# Install package dalam mode editable dengan semua dependencies
pip install -e ".[all]"
```

Atau instal dengan kategori spesifik:

```bash
# Hanya dependencies development
pip install -e ".[dev]"

# Development + Machine Learning
pip install -e ".[dev,ml]"

# Development + Dashboard
pip install -e ".[dev,dashboard]"

# Development + API clients
pip install -e ".[dev,api]"
```

### Opsi 3: Menggunakan requirements.txt (Minimal)

Untuk instalasi minimal tanpa optional dependencies:

```bash
pip install -r requirements.txt
```

## 🎯 Quick Start Testing

Setelah instalasi selesai, jalankan tests:

```bash
# Jalankan semua tests
pytest

# Jalankan tests dengan coverage report
pytest --cov=wunaraha --cov-report=html

# Jalankan tests dengan verbose output
pytest -v

# Jalankan test spesifik
pytest tests/test_auditor.py
```

## 🛠️ Development Tools

Setelah instalasi, Anda dapat menggunakan tools berikut:

### Code Formatting
```bash
# Format code dengan Black
black wunaraha/ tests/

# Sort imports dengan isort
isort wunaraha/ tests/
```

### Code Linting
```bash
# Check code style dengan flake8
flake8 wunaraha/ tests/

# Type checking dengan mypy
mypy wunaraha/
```

### Pre-commit Hooks
```bash
# Install pre-commit hooks
pre-commit install

# Run pre-commit manually
pre-commit run --all-files
```

## 📦 Struktur Dependencies

### Core Dependencies (Wajib)
- `transformers` - Model AI untuk validasi
- `torch` - Deep learning framework
- `pandas` - Data processing
- `numpy` - Numerical computing
- `requests` - HTTP client

### Testing Dependencies
- `pytest` - Testing framework
- `pytest-cov` - Coverage reporting
- `pytest-asyncio` - Async test support

### Development Tools
- `black` - Code formatter
- `flake8` - Code linter
- `mypy` - Type checker
- `isort` - Import sorter
- `pre-commit` - Git hooks manager

### Optional Dependencies

#### Machine Learning
- `scikit-learn` - ML utilities
- `sentence-transformers` - Sentence embeddings

#### Dashboard & Visualization
- `streamlit` - Web dashboard
- `plotly` - Interactive plots

#### API Clients
- `tweepy` - Twitter API
- `Mastodon.py` - Mastodon API
- `python-dotenv` - Environment variables

#### Utilities
- `ipython` - Interactive Python shell
- `jupyter` - Jupyter notebooks

## 🔍 Verifikasi Instalasi

Setelah instalasi, verifikasi bahwa semua package terinstall:

```bash
# Cek versi Python
python --version

# List semua installed packages
pip list

# Cek package spesifik
pip show pytest
pip show transformers
```

## 🐛 Troubleshooting

### Issue: torch installation gagal
```bash
# Install torch dari PyTorch index
pip install torch>=2.0.0 --index-url https://download.pytorch.org/whl/cpu
```

### Issue: dependencies conflict
```bash
# Upgrade pip terlebih dahulu
pip install --upgrade pip

# Clear cache dan reinstall
pip cache purge
pip install -r requirements-dev.txt --no-cache-dir
```

### Issue: permission error
```bash
# Gunakan user install
pip install -r requirements-dev.txt --user

# Atau gunakan virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Linux/Mac
# atau
venv\Scripts\activate  # Windows
pip install -r requirements-dev.txt
```

## 💡 Best Practices

1. **Gunakan Virtual Environment** - Selalu gunakan venv atau conda untuk mengisolasi dependencies
2. **Pin Versions** - Untuk production, pertimbangkan untuk pin versi spesifik
3. **Regular Updates** - Update dependencies secara berkala untuk security patches
4. **Test Before Commit** - Selalu jalankan tests sebelum commit perubahan

## 📝 Contoh Penggunaan

```python
# Import library setelah instalasi
from wunaraha import Auditor

# Initialize auditor
auditor = Auditor()

# Run validation
result = auditor.validate("your-text-here")
print(result)
```

## 🆘 Butuh Bantuan?

- Dokumentasi: Lihat README.md
- Issues: https://github.com/wunaraha/wunaraha/issues
- Contributing: Lihat CONTRIBUTING.md
