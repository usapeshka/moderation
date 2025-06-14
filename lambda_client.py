import os
import requests
import json 
from dotenv import load_dotenv
import base64
from openai import OpenAI

load_dotenv()  # loads .env

API_KEY = os.getenv("LAMBDA_API_KEY")
API_URL = "https://api.lambda.ai/v1"  # Use the correct base URL for OpenAI client

client = OpenAI(
    api_key=API_KEY,
    base_url=API_URL,
)

def call_lambda(model_name: str, prompt: str, image_bytes: bytes = None) -> dict:
    """
    Calls Lambda.ai inference API using OpenAI client.
    :param model_name: name of the model to use
    :param prompt: textual prompt
    :param image_bytes: optional image content
    :return: JSON response dict
    """
    # Prepare the message for chat completion
    if image_bytes:
        # Encode image as base64 data URI
        encoded = base64.b64encode(image_bytes).decode("utf-8")
        image_data_uri = f"data:image/jpeg;base64,{encoded}"
        message = {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
                {"type": "image_url", "image_url": {"url": image_data_uri}},
            ],
        }
    else:
        message = {
            "role": "user",
            "content": [
                {"type": "text", "text": prompt},
            ],
        }
    try:
        chat_response = client.chat.completions.create(
            model=model_name,
            messages=[message],
        )
        # Return the model's response content
        #return {"result": chat_response.choices[0].message.content}
        return chat_response
    except Exception as e:
        print("Error:", e)
        return {"error": str(e)}
