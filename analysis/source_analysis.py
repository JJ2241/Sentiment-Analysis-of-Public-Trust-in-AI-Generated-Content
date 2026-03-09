import pandas as pd
from urllib.parse import urlparse

# load sentiment dataset
df = pd.read_csv("data/final/sentiment_results.csv")

# extract domain name
def get_source(url):
    domain = urlparse(url).netloc
    domain = domain.replace("www.", "")
    return domain.split(".")[0]

df["source"] = df["url"].apply(get_source)

# save dataset with source
df.to_csv("data/final/source_dataset.csv", index=False)

print(df["source"].value_counts().head(10))

# sentiment by source
sentiment_source = pd.crosstab(
    df["source"],
    df["sentiment"]
)

print("\nSentiment by Source\n")
print(sentiment_source)

sentiment_source.to_csv(
    "outputs/source_sentiment_table.csv"
)