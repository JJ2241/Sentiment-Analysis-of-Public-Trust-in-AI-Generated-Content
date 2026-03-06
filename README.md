# Sentiment Analysis of Public Trust in AI-Generated Content

## Project Overview

This project builds an automated pipeline to **collect, process, and analyze news articles discussing AI-generated content**. The objective is to study **public trust, credibility concerns, and sentiment toward generative AI technologies** using Natural Language Processing (NLP).

The system scrapes news articles from search engines, processes the content into paragraph-level samples, filters AI-trust related discussions, reconstructs articles, and performs **sentiment analysis**.

This workflow produces a dataset and analytical outputs suitable for **academic research on AI perception and media trust**.

---

# Research Objective

The goal of this study is to analyze **how news media frames AI-generated content**, focusing on:

* Trust and credibility of AI-generated media
* Misinformation and deepfake concerns
* Ethical and regulatory debates around AI
* Overall sentiment toward generative AI technologies

---

# Project Pipeline

The system follows the pipeline below:

```
News Scraping
      ↓
Raw Dataset
      ↓
Text Cleaning
      ↓
AI Trust Filtering
      ↓
Article Reconstruction
      ↓
Sentiment Analysis
      ↓
Visualization / Insights
```

---

# Project Structure

```
ai-trust-sentiment-analysis
│
├── scraping
│   └── large_scale_news_scraper.py
│
├── preprocessing
│   ├── clean_text.py
│   ├── filter_ai_trust.py
│   └── rebuild_articles.py
│
├── analysis
│   └── sentiment_analysis.py
│
├── visualization
│   └── sentiment_chart.py
│
├── data
│   ├── raw
│   ├── processed
│   └── final
│
├── outputs
│   └── figures
│
├── pipeline.py
├── requirements.txt
└── README.md
```

---

# Installation

## 1. Clone the Repository

```
git clone <repository-url>
cd ai-trust-sentiment-analysis
```

## 2. Create a Virtual Environment

```
python -m venv venv
```

Activate the environment:

**Windows**

```
venv\Scripts\activate
```

**Mac/Linux**

```
source venv/bin/activate
```

## 3. Install Dependencies

```
pip install -r requirements.txt
```

---

# Download NLP Resources

Run once:

```
python
```

```
import nltk
nltk.download("punkt")
nltk.download("stopwords")
```

---

# Running the Pipeline

To execute the entire workflow:

```
python pipeline.py
```

The pipeline automatically performs:

1. News scraping
2. Text preprocessing
3. AI-trust filtering
4. Article reconstruction
5. Sentiment analysis

---

# Output Files

After execution, the following datasets will be generated:

### Raw Dataset

```
data/raw/large_news_dataset.csv
```

### Clean Dataset

```
data/processed/clean_dataset.csv
```

### Filtered AI Trust Dataset

```
data/processed/ai_trust_dataset.csv
```

### Article-Level Dataset

```
data/final/article_dataset.csv
```

### Sentiment Results

```
data/final/sentiment_results.csv
```

---

# Sentiment Analysis

Sentiment is calculated using **VADER Sentiment Analysis**, which is well suited for news and social media text.

Each article receives one of three sentiment labels:

* **Positive**
* **Negative**
* **Neutral**

---

# Visualization

Sentiment distribution charts are saved in:

```
outputs/figures/
```

These visualizations can be used directly in research reports or presentations.

---

# Expected Dataset Size

| Stage                        | Typical Size   |
| ---------------------------- | -------------- |
| Raw paragraphs               | 8,000 – 20,000 |
| Filtered AI-trust paragraphs | 3,000 – 6,000  |
| Article-level dataset        | 200 – 500      |

---

# Research Applications

This dataset and pipeline can be used for:

* Sentiment analysis of AI discourse
* Media framing studies
* AI ethics research
* Misinformation and deepfake analysis
* Topic modeling of AI discussions

---

# Future Improvements

Possible extensions include:

* Topic modeling using LDA
* Named Entity Recognition for AI actors
* Temporal analysis of sentiment trends
* Cross-platform comparison with social media data
* Advanced sentiment models using transformers

---

# Author

This project was developed by Junaid Kazi as part of a **Master’s research project in Data Science and Business Analytics**, focusing on **public perception of generative AI technologies**.

---
