import json

from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)


SYSTEM_PROMPT = """
You are an expert AI News Editor.

Analyze the article and return ONLY valid JSON.

{
    "headline":"",
    "executive_summary":"",
    "why_it_matters":"",
    "importance_score":0,
    "confidence":0,
    "business_impact":"",
    "future_outlook":"",
    "tags":[]
}
"""


def analyze_article(article):

    prompt = f"""
Title:
{article['title']}

Summary:
{article['summary']}

Source:
{article['source']}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=SYSTEM_PROMPT + prompt
    )

    text = response.text.strip()

    # Remove markdown if Gemini wraps JSON
    text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)