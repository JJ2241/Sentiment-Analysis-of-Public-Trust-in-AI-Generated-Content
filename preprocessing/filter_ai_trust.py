import pandas as pd

keywords = [
    "trust","credibility","reliable","reliability","confidence",
    "authentic","authenticity",
    "misinformation","disinformation","fake","fake news","deepfake",
    "manipulated media",
    "generative ai","ai generated","synthetic media","ai content",
    "ai writing","ai journalism","ai article",
    "hallucination","bias","algorithmic bias",
    "regulation","policy","governance","accountability","transparency","ethics"
]

df = pd.read_csv("data/processed/clean_news_dataset.csv")

mask = df["clean_text"].str.contains("|".join(keywords), case=False)

filtered = df[mask]

filtered.to_csv("data/processed/ai_trust_dataset.csv", index=False)

print("Filtered dataset size:", len(filtered))