# mistral_client.py
import requests
from config import MISTRAL_API_URL, OPENAI_API_KEY


def call_mistral(prompt):
    # Placeholder for actual Mistral API call
    headers = {
        "Authorization": f"Bearer {OPENAI_API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {"prompt": prompt}
    response = requests.post(MISTRAL_API_URL, json=payload, headers=headers)
    if response.status_code == 200:
        return response.json().get("text", "")
    else:
        return "Error: Mistral request failed."
