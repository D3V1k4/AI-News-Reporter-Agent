KEYWORDS = {
    "release": 4,
    "launch": 4,
    "funding": 5,
    "research": 3,
    "gpt": 5,
    "gemini": 5,
    "claude": 5,
    "llama": 5,
    "breakthrough": 5,
    "nvidia": 4,
}


def calculate_score(article):
    score = 0

    text = (article["title"] + " " + article["summary"]).lower()

    for keyword, value in KEYWORDS.items():
        if keyword in text:
            score += value

    return score