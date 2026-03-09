import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/final/source_dataset.csv")

# sentiment counts per source
table = pd.crosstab(df["source"], df["sentiment"])

# keep top sources
top_sources = df["source"].value_counts().head(8).index
table = table.loc[top_sources]

# ensure consistent column order
table = table[["positive", "neutral", "negative"]]

# RGB colors (normalized to 0–1 for matplotlib)
colors = [
    (52/255,120/255,246/255),   # positive - blue
    (160/255,160/255,160/255),  # neutral - gray
    (204/255,53/255,69/255)     # negative - red
]

ax = table.plot(
    kind="bar",
    stacked=True,
    figsize=(10,6),
    color=colors
)

plt.title("Sentiment Distribution by News Source")
plt.xlabel("News Source")
plt.ylabel("Number of Articles")

plt.xticks(rotation=45)

# add count labels but hide zeros
for container in ax.containers:
    labels = [
        str(int(v)) if v > 0 else ""
        for v in container.datavalues
    ]

    ax.bar_label(
        container,
        labels=labels,
        label_type="center",
        fontsize=9
    )

plt.tight_layout()

plt.savefig("outputs/figures/source_sentiment_chart.png")

plt.show()