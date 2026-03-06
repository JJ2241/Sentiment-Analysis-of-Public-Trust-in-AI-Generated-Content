import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

df = pd.read_csv("data/final/sentiment_results.csv")

# -----------------------
# Sentiment Distribution
# -----------------------

counts = df["sentiment"].value_counts()

plt.figure()

counts.plot(kind="bar")

plt.title("Sentiment Distribution of AI-Generated Content Discussions")

plt.xlabel("Sentiment")

plt.ylabel("Number of Articles")

plt.savefig("outputs/figures/sentiment_bar_chart.png")

plt.close()


# -----------------------
# Sentiment Pie Chart
# -----------------------

plt.figure()

plt.pie(counts, labels=counts.index, autopct="%1.1f%%")

plt.title("Sentiment Distribution")

plt.savefig("outputs/figures/sentiment_pie_chart.png")

plt.close()


# -----------------------
# Word Cloud
# -----------------------

text = " ".join(df["article_text"])

wordcloud = WordCloud(
    width=1000,
    height=500,
    background_color="white"
).generate(text)

plt.figure(figsize=(10,5))

plt.imshow(wordcloud)

plt.axis("off")

plt.savefig("outputs/figures/wordcloud.png")

plt.close()

print("Visualizations saved to outputs/figures/")