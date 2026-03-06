import subprocess
import time

steps = [

    ("Scraping News Articles",
     "scraping/large_scale_news_scraper.py"),

    ("Cleaning Text",
     "preprocessing/clean_text.py"),

    ("Filtering AI Trust Content",
     "preprocessing/filter_ai_trust.py"),

    ("Rebuilding Articles",
     "preprocessing/rebuild_articles.py"),

    ("Running Sentiment Analysis",
     "analysis/sentiment_analysis.py"),

    ("Generating Visualizations",
     "visualization/generate_visuals.py")
]

print("\nStarting AI Trust Sentiment Pipeline\n")

for name, script in steps:

    print(f"\nRunning: {name}")

    result = subprocess.run(["python", script])

    if result.returncode != 0:
        print(f"Error occurred during: {name}")
        break

    time.sleep(2)

print("\nPipeline completed.\n")