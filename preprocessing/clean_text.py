import pandas as pd
import re

df = pd.read_csv("data/raw/large_news_dataset.csv")

def clean_text(text):

    text = text.lower()

    text = re.sub(r"http\S+", "", text)

    text = re.sub(r"[^a-z\s]", "", text)

    text = re.sub(r"\s+", " ", text)

    return text.strip()


df["clean_text"] = df["paragraph"].apply(clean_text)

df.to_csv("data/processed/clean_news_dataset.csv", index=False)

print("Clean dataset saved.")