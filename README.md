<!-- altmetric-validator-ai/README.md -->

# 🛡️ Wunaraha: Framework Audit Halusinasi Metrik Alternatif

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![Hugging Face](https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Transformers-yellow)](https://huggingface.co/)

> *"Apakah mereka benar-benar membaca abstraknya, atau hanya membaca judulnya?"*

**Wunaraha** adalah *tools* untuk membuktikan bahwa metrik alternatif (Altmetrics: Mention Twitter, Berita, Paten) juga rentan terhadap manipulasi bot dan *hype cycle*. Kami menggunakan AI untuk **membedakan antara Buzz Viral (Kebisingan) vs. Intellectual Adoption (Adopsi Intelektual)**.

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

### 📦 Instalasi & Penggunaan

```bash
git clone https://github.com/stipwunaraha/altmetric-validator-ai.git
cd altmetric-validator-ai
pip install -r requirements.txt
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

### 🚧 Roadmap
- [ ] Integrasi Twitter API v2 dan Mastodon API.
- [ ] Model klasifikasi *depth-of-engagement* berbasis **DeBERTa**.
- [ ] Dashboard Streamlit untuk visualisasi hasil audit.
- [ ] Dukungan untuk menganalisis berita dari Google News RSS.

### 📚 Referensi
- *Quantitative Methods in Research Evaluation Citation Indicators, Altmetrics, and Artificial Intelligence* (Thelwall, 2024).
- *Have we reached the limits of altmetrics?* (Research Information, 2023).

### 🤝 Kontribusi
Kami mencari *data scientist* dan *NLP engineer* yang tertarik dengan *research integrity*.

### 📄 Lisensi
MIT License.
