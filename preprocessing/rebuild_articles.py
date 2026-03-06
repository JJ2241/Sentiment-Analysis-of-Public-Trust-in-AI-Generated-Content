import pandas as pd

# load dataset
df = pd.read_csv("data/processed/ai_trust_dataset.csv")

# group paragraphs by article url
article_df = df.groupby("url").agg({
    "title": "first",
    "paragraph": lambda x: " ".join(x)
}).reset_index()

# rename column
article_df.rename(columns={"paragraph": "article_text"}, inplace=True)

# save new dataset
article_df.to_csv("data/final/article_level_dataset.csv", index=False)

print("Total articles:", len(article_df))
print("Dataset saved to data/final/article_level_dataset.csv")