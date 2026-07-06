import requests
import os
from config import OPENROUTER_API_KEY


def openrouter_roadmap(course_name):
    """
    Roadmap banane ke liye OpenRouter API ko call karega.
    """
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "gpt-3.5-turbo",  # sahi model name
        "messages": [
            {"role": "system", "content": "You are an expert career counselor."},
            {"role": "user", "content": f"""
Generate a clear step-by-step learning roadmap for the course '{course_name}'.
The roadmap must be:
1. In English only (no Hindi or Hinglish).
2. Well-structured with numbered steps.
3. Each step should have a brief description and estimated duration.
4. Format it in clean bullet points or numbered list.
"""}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        roadmap_text = response.json()["choices"][0]["message"]["content"]
        return roadmap_text
    except Exception as e:
        return f"Error fetching roadmap: {e}"
