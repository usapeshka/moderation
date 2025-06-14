import streamlit as st
from lambda_client import call_lambda
from utils import load_image, display_response

def main():
    st.title("🐾 Lambda.ai + Streamlit Demo")

    # Model switcher
    model = st.selectbox("Select model", ["llama3.2-11b-vision-instruct"])
    
    prompt = st.text_input("Enter your text prompt", "")

    uploaded_file = st.file_uploader("Upload an image (optional)", type=["jpg", "jpeg", "png"])
    image_bytes = load_image(uploaded_file)

    if st.button("Submit"):
        if not prompt and not image_bytes:
            st.error("Please provide a prompt, an image, or both.")
            return
        
        with st.spinner("Calling Lambda.ai..."):
            res = call_lambda(model_name=model, prompt=prompt, image_bytes=image_bytes)
        
        display_response(res)

if __name__ == "__main__":
    main()
