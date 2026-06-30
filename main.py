from agents.collector import fetch_news
from agents.duplicate import remove_duplicates
from agents.category import categorize
from agents.company import extract_companies
from agents.ranker import calculate_score
from agents.emailer import send_email
from database.database import (
    create_table,
    save_articles,
    get_articles
)
from agents.newsletter import generate_newsletter

newsletter_articles = []

news = fetch_news()

print(f"\nCollected: {len(news)} articles")

news = remove_duplicates(news)

print(f"After duplicates removed: {len(news)}\n")

for article in news:
    article["category"] = categorize(article)
    article["companies"] = extract_companies(article)
    article["score"] = calculate_score(article)

news.sort(key=lambda x: x["score"], reverse=True)

# Create the database table (only if it doesn't exist)
create_table()

# Save all processed articles
save_articles(news)


from agents.gemini_agent import analyze_article

print("\nAnalyzing Today's Top 5 Articles...\n")

# Analyze only the first 5 collected articles
for i, article in enumerate(news[:5], start=1):

    print("=" * 80)
    print(f"ARTICLE {i}")
    print("=" * 80)

    try:
        analysis = analyze_article(article)
        newsletter_articles.append(analysis)

        print(f"Headline: {analysis['headline']}")
        print(f"Summary: {analysis['executive_summary']}")
        print(f"Why It Matters: {analysis['why_it_matters']}")
        print(f"Importance: {analysis['importance_score']}/10")
        print(f"Business Impact: {analysis['business_impact']}")
        print(f"Future Outlook: {analysis['future_outlook']}")
        print(f"Tags: {', '.join(analysis['tags'])}")

    except Exception as e:
        print("Error:", e)

html = generate_newsletter(newsletter_articles)

with open("newsletter_preview.html", "w", encoding="utf8") as f:
    f.write(html)

print("\n✅ Newsletter generated successfully!")
send_email(html)
