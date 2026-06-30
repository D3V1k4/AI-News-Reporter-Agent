import feedparser

RSS_FEEDS = {
    "OpenAI": "https://openai.com/news/rss.xml",
    "Hugging Face": "https://huggingface.co/blog/feed.xml",
    "MIT News": "https://news.mit.edu/rss/topic/artificial-intelligence2"
}


def fetch_news():
    all_news = []

    for source, url in RSS_FEEDS.items():
        print(f"Fetching news from {source}...")

        feed = feedparser.parse(url)

        for article in feed.entries[:10]:
            news = {
                "title": article.get("title", "No Title"),
                "link": article.get("link", ""),
                "published": article.get("published", "Unknown"),
                "summary": article.get("summary", ""),
                "source": source,
            }

            all_news.append(news)

    return all_news