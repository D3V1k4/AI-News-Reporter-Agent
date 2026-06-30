from datetime import datetime


def generate_newsletter(articles):

    article_html = ""

    for article in articles:

        article_html += f"""
        <div class="article">

        <h2>{article['headline']}</h2>

        <p><b>Summary</b></p>

        <p>{article['executive_summary']}</p>

        <p><b>Why It Matters</b></p>

        <p>{article['why_it_matters']}</p>

        <p class="score">

        Importance:
        {article['importance_score']}/10

        </p>

        <p>

        <b>Future Outlook</b>

        </p>

        <p>

        {article['future_outlook']}

        </p>

        </div>
        """

    with open("templates/newsletter.html","r",encoding="utf8") as f:

        html = f.read()

    html = html.replace(
        "{{DATE}}",
        datetime.now().strftime("%d %B %Y")
    )

    html = html.replace(
        "{{SUMMARY}}",
        "Today's newsletter is automatically generated using Gemini AI."
    )

    html = html.replace(
        "{{ARTICLES}}",
        article_html
    )

    return html