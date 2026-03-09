import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# load dataset
df = pd.read_csv("data/final/article_dataset.csv")

texts = df["article_text"].astype(str)

# TF-IDF vectorizer
vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=1000
)

X = vectorizer.fit_transform(texts)

# get feature names
words = vectorizer.get_feature_names_out()

# sum scores
scores = X.sum(axis=0).A1

word_scores = list(zip(words, scores))

# sort by importance
word_scores = sorted(word_scores, key=lambda x: x[1], reverse=True)

top_words = word_scores[:30]

print("\nTop Keywords:\n")

for word, score in top_words:
    print(word, round(score, 2))

keywords_df = pd.DataFrame(top_words, columns=["keyword","score"])

keywords_df.to_csv(
    "outputs/topic_keywords.csv",
    index=False
)