# # utils/course_recommender.py
# import openai
# from config import OPENROUTER_API_KEY

# openai.api_key = OPENROUTER_API_KEY
# openai.api_base = "https://openrouter.ai/api/v1"

# def openrouter_course_recommendation(interest, goal, marks):
#     prompt = f"""
# Act as an expert Indian career counselor.

# Suggest **3 college-level courses** based on:
# - Student Interest: {interest}
# - Career Goal: {goal}
# - 12th Marks: {marks}%

# ⚠ Return output in this exact format only:
# 1. Course Name - Reason (1 line)
# 2. Course Name - Reason (1 line)
# 3. Course Name - Reason (1 line)
# """
#     response = openai.ChatCompletion.create(
#         model="openai/gpt-3.5-turbo",
#         messages=[{"role": "user", "content": prompt}]
#     )
#     return response['choices'][0]['message']['content']


# utils/course_recommender.py
import requests
from config import OPENROUTER_API_KEY

BASE_URL = "https://openrouter.ai/api/v1/chat/completions"

def openrouter_course_recommendation(interest, goal, marks):
    """Fetch 3 college-level course recommendations from OpenRouter API."""

    prompt = f"""
Act as an expert Indian career counselor.

Suggest **3 college-level courses** based on:
- Student Interest: {interest}
- Career Goal: {goal}
- 12th Marks: {marks}%

⚠ Return output in this exact format only:
1. Course Name - Reason (1 line)
2. Course Name - Reason (1 line)
3. Course Name - Reason (1 line)
"""

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openai/gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a helpful career counselor for Indian students."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(BASE_URL, headers=headers, json=payload)
        response.raise_for_status()
        data = response.json()

        # Extract message content
        return data["choices"][0]["message"]["content"]

    except Exception as e:
        return f"Error fetching course recommendations: {e}"
