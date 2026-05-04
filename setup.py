"""
Setup script untuk Wunaraha - Altmetric Validator AI
Untuk instalasi development di localhost
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="wunaraha",
    version="0.1.0",
    author="Wunaraha Contributors",
    author_email="wunaraha@example.com",
    description="Wunaraha: Framework Audit Halusinasi Metrik Alternatif",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/wunaraha/wunaraha",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    python_requires=">=3.8",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
        "ml": [
            "scikit-learn>=1.2.0",
            "sentence-transformers>=2.2.0",
        ],
        "dashboard": [
            "streamlit>=1.20.0",
            "plotly>=5.14.0",
        ],
        "api": [
            "tweepy>=4.14.0",
            "Mastodon.py>=1.5.0",
            "python-dotenv>=1.0.0",
        ],
    },
)
