import pandas as pd
from sentiment_utils import article_sentiment


df = pd.read_csv("data/final/article_level_dataset.csv")

df["sentiment"] = df["article_text"].apply(article_sentiment)

df.to_csv("data/final/sentiment_results.csv", index=False)

print("\nSentiment Distribution\n")

print(df["sentiment"].value_counts())