import streamlit as st
import requests
from PIL import Image
from io import BytesIO

st.set_page_config(page_title="Image Processing App", layout="wide")

st.title("Image Processing with FastAPI")

# URL de l'API FastAPI
api_url = "http://localhost:8000/upload_image"

st.markdown("### Upload an Image")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # Afficher l'image téléchargée
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    # Préparer la requête pour l'API FastAPI
    files = {"file": uploaded_file.getvalue()}
    response = requests.post(api_url, files=files)

    # Afficher l'image traitée
    if response.status_code == 200:
        st.image(response.content, caption="Processed Image", use_column_width=True)
    else:
        st.write("Failed to process image")
