COMPANIES = [
    "OpenAI",
    "Google",
    "Microsoft",
    "Meta",
    "Anthropic",
    "NVIDIA",
    "Apple",
    "Amazon",
    "xAI",
]


def extract_companies(article):
    text = (article["title"] + " " + article["summary"]).lower()

    found = []

    for company in COMPANIES:
        if company.lower() in text:
            found.append(company)

    return found