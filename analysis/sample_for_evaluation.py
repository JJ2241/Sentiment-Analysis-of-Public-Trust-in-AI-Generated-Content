import pandas as pd

df = pd.read_csv("data/final/sentiment_results.csv")

sample = df.sample(50, random_state=42)

sample.to_csv("outputs/evaluation_sample.csv", index=False)

print("Sample saved for manual labeling.")