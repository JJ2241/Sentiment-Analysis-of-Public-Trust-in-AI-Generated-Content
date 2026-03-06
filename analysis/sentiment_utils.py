import nltk
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()

# AI-risk keywords
negative_keywords = [
    "misinformation",
    "disinformation",
    "deepfake",
    "fake news",
    "hallucination",
    "bias",
    "manipulation",
    "propaganda",
    "deception",
]

positive_keywords = [
    "innovation",
    "breakthrough",
    "improvement",
    "benefit",
    "advancement",
    "opportunity",
]


def article_sentiment(text):

    text_lower = str(text).lower()

    # Rule-based override
    if any(word in text_lower for word in negative_keywords):
        return "negative"

    if any(word in text_lower for word in positive_keywords):
        return "positive"

    # fallback to vader
    score = analyzer.polarity_scores(text_lower)["compound"]

    if score >= 0.2:
        return "positive"
    elif score <= -0.2:
        return "negative"
    else:
        return "neutral"