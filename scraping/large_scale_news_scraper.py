import requests
from bs4 import BeautifulSoup
from newspaper import Article
import pandas as pd
from tqdm import tqdm
import time

headers = {
    "User-Agent": "Mozilla/5.0"
}

# Expanded research queries
queries = [
    "generative AI trust news",
    "AI generated content credibility",
    "AI misinformation news",
    "deepfake media trust",
    "AI journalism ethics",
    "AI fake news concerns",
    "public trust artificial intelligence media",
    "AI regulation policy news",
    "AI transparency accountability",
    "AI hallucination problems",
    "AI content authenticity debate",
    "impact of generative AI journalism",
    "AI misinformation social media",
    "deepfake political misinformation",
    "AI ethics debate news",
]

def collect_links(query, pages=50):

    links = []

    for page in range(pages):

        start = page * 10

        url = f"https://www.bing.com/news/search?q={query}&first={start}"

        try:

            r = requests.get(url, headers=headers)

            soup = BeautifulSoup(r.text, "html.parser")

            results = soup.select("a.title")

            for r in results:

                link = r.get("href")

                if link and link.startswith("http"):
                    links.append(link)

        except:
            continue

        time.sleep(1)

    return list(set(links))


print("\nCollecting article links...\n")

all_links = []

for q in queries:

    links = collect_links(q, pages=25)

    print(q, "→", len(links), "links")

    all_links.extend(links)

all_links = list(set(all_links))

print("\nTotal unique links:", len(all_links))


dataset = []

print("\nDownloading articles...\n")

for link in tqdm(all_links):

    try:

        article = Article(link)

        article.download()

        article.parse()

        paragraphs = article.text.split("\n")

        for p in paragraphs:

            p = p.strip()

            if len(p) > 120:

                dataset.append({
                    "title": article.title,
                    "paragraph": p,
                    "url": link
                })

        time.sleep(1)

    except:
        continue


df = pd.DataFrame(dataset)

df = df.drop_duplicates(subset=["paragraph"])

print("\nTotal paragraphs collected:", len(df))

df.to_csv("data/raw/large_news_dataset.csv", index=False)

print("\nDataset saved to data/raw/large_news_dataset.csv")