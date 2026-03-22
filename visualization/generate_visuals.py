import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

# Load dataset
df = pd.read_csv("data/final/sentiment_results.csv")

df["article_text"] = df["article_text"].fillna("")

# -----------------------
# Sentiment Distribution Bar Chart
# -----------------------

sentiment_order = ["negative","positive", "neutral"]
counts = df["sentiment"].value_counts().reindex(sentiment_order, fill_value=0)

colors = [
    (204/255,53/255,69/255),     # Negative - Red
    (52/255,120/255,246/255),   # Positive - Blue
    (160/255,160/255,160/255)  # Neutral - Gray
]

plt.figure(figsize=(12,6))

ax = counts.plot(kind="bar", color=colors)

plt.title("Sentiment Distribution of AI-Generated Content Discussions")

plt.xlabel("Sentiment")

plt.ylabel("Number of Articles")

plt.xticks(rotation=30)

# add counts above bars
for i, v in enumerate(counts):
    ax.text(i, v + 1, str(v), ha='center', fontsize=11)

plt.tight_layout()

plt.savefig(
    "outputs/figures/sentiment_bar_chart.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.close()

# -----------------------
# Sentiment Pie Chart
# -----------------------

plt.figure(figsize=(8,8))

plt.pie(
    counts,
    labels=counts.index,
    autopct="%1.1f%%",
    colors=colors,
    startangle=90
)

plt.title("Sentiment Distribution")

plt.tight_layout()

plt.savefig(
    "outputs/figures/sentiment_pie_chart.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.close()

# -----------------------
# Word Cloud
# -----------------------

text = " ".join(df["article_text"])

wordcloud = WordCloud(
    width=3840,
    height=2160,
    background_color="white"
).generate(text)

plt.figure(figsize=(16,9))

plt.imshow(wordcloud)

plt.axis("off")

plt.title("Word Cloud of Generative AI News Coverage")

plt.tight_layout()

plt.savefig(
    "outputs/figures/wordcloud.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

plt.close()

print("4K visualizations saved to outputs/figures/")