def remove_duplicates(news_list):
    unique_news = []
    seen_links = set()

    for article in news_list:
        link = article["link"]

        if link not in seen_links:
            seen_links.add(link)
            unique_news.append(article)

    return unique_news