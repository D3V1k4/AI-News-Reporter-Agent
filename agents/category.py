CATEGORIES = {
    "LLM": ["gpt", "llama", "gemini", "claude", "mistral"],
    "Computer Vision": ["vision", "image", "object detection"],
    "Robotics": ["robot", "robotics"],
    "Research": ["paper", "research", "study"],
    "Hardware": ["gpu", "nvidia", "chip", "processor"],
}


def categorize(article):
    text = (article["title"] + " " + article["summary"]).lower()

    for category, keywords in CATEGORIES.items():
        for keyword in keywords:
            if keyword in text:
                return category

    return "General"