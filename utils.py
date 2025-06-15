import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv


def load_image(uploaded_file):
    """
    Read bytes from uploaded image file.
    """
    if uploaded_file is not None:
        return uploaded_file.read()
    return None

def display_response(resp: dict):
    """
    Streamlit display logic.
    """
    st.json(resp)


def get_lambda_model_ids():
    load_dotenv()  # Load environment variables from .env file
    api_key = os.getenv("LAMBDA_API_KEY")
    api_base = os.getenv("LAMBDA_API_URL")
    
    if not api_key:
        raise ValueError("LAMBDA_API_KEY environment variable is not set.")
    client = OpenAI(api_key=api_key, base_url=api_base)
    models = client.models.list()
    print(models)  # Debug: print the models list
    # Extract model IDs
    return [m.id for m in models.data]
