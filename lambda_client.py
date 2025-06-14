import os
import requests
from dotenv import load_dotenv

load_dotenv()  # loads .env

API_KEY = os.getenv("LAMBDA_API_KEY")
API_URL = os.getenv("LAMBDA_API_URL")

def call_lambda(model_name: str, prompt: str, image_bytes: bytes = None) -> dict:
    """
    Calls Lambda.ai inference API.
    :param model_name: name of the model to use
    :param prompt: textual prompt
    :param image_bytes: optional image content
    :return: JSON response dict
    """
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {
        "model": model_name,
        "prompt": prompt,
    }
    # For image + prompt tasks, you'll need multipart or a specific schema.
    if image_bytes:
        files = {
            "image": ("uploaded.jpg", image_bytes, "image/jpeg"),
            "data": (None, json.dumps(payload), "application/json")
        }
        response = requests.post(API_URL, headers={"Authorization": f"Bearer {API_KEY}"}, files=files)
    else:
        response = requests.post(API_URL, headers=headers, json=payload)
    return response.json()
