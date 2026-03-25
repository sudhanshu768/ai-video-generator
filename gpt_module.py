import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def generate_script(prompt):
    url = "https://openrouter.ai/api/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openrouter/auto",
        "messages": [
            {
                "role": "system",
                "content": "You are a cinematic storyteller."
            },
            {
                "role": "user",
                "content": f"""
Write a cinematic short story for a YouTube video.

Topic: {prompt}

Rules:
- 5 to 6 scenes
- Each scene = 1–2 lines
- DO NOT write 'Scene 1'
- Just write lines separated by newline
- Strong visuals, emotional, dramatic

Example:
A storm rages over a silent city.
Lightning reveals empty streets.

A lone robot looks at the sky.
Its eyes flicker with confusion.
"""
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    print("API Response:", data)

    try:
        return data["choices"][0]["message"]["content"]
    except:
        return "AI failed to generate script."


# 🔥 IMPORTANT: make image prompts DIRECT (no over-refinement)
def refine_image_prompt(line):
    return f"{line}, cinematic lighting, ultra realistic, 4k, detailed"