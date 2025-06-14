import streamlit as st

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
