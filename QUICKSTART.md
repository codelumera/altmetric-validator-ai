# 🚀 Quick Start - Wunaraha

Panduan cepat untuk mulai menggunakan Wunaraha dalam 5 menit!

## Langkah 1: Clone & Setup Environment

```bash
# Clone repository
git clone https://github.com/wunaraha/wunaraha.git
cd wunaraha

# Buat virtual environment
python -m venv venv

# Aktifkan virtual environment
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

## Langkah 2: Install Dependencies

**Opsi A: Instalasi Lengkap (Rekomendasi)**
```bash
pip install -e ".[all]"
```

**Opsi B: Instalasi Minimal (Core Only)**
```bash
pip install -e .
```

**Opsi C: Dari requirements.txt**
```bash
pip install -r requirements.txt
```

## Langkah 3: Verifikasi Instalasi

```bash
# Jalankan test sederhana
python -c "from wunaraha import AltmetricAuditor; print('✅ Wunaraha siap digunakan!')"

# Atau jalankan example
python example_usage.py
```

## Langkah 4: Mulai Coding!

```python
from wunaraha import AltmetricAuditor
from wunaraha.models import Mention

# Buat auditor
auditor = AltmetricAuditor(mode="rule_based")

# Audit DOI (dengan mock data)
report = auditor.audit("10.1234/example.2024.001")

# Lihat hasil
print(f"Purity Score: {report.purity_score:.2%}")
print(f"Total Mentions: {report.total_mentions}")
```

## Langkah 5: Jalankan Tests (Opsional)

```bash
# Jalankan semua tests
pytest

# Dengan coverage report
pytest --cov=wunaraha --cov-report=html
```

## 🎯 Command Cheat Sheet

```bash
# Install development version
pip install -e ".[dev]"

# Format code
black wunaraha/ tests/
isort wunaraha/ tests/

# Lint code
flake8 wunaraha/ tests/

# Type check
mypy wunaraha/

# Run tests
pytest
pytest -v              # Verbose mode
pytest -x              # Stop on first failure
pytest --cov=wunaraha  # With coverage

# Pre-commit hooks
pre-commit install
pre-commit run --all-files
```

## 📚 Dokumentasi Lengkap

- Panduan instalasi detail: `INSTALL.md`
- Contoh penggunaan: `example_usage.py`
- README utama: `README.md`

## ❓ Troubleshooting

**Error: Module not found**
```bash
pip install -e ".[all]"
```

**Error: Python version**
```bash
# Pastikan Python 3.8+
python --version
```

**Need help?**
- Check issues: https://github.com/wunaraha/wunaraha/issues
- Read INSTALL.md for detailed troubleshooting
