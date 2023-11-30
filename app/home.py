import streamlit as st
from PIL import Image
import requests


st.title("Epicure AI")
st.write("Revolutionize your culinary experience with AI")


# Upload image through Streamlit
uploaded_image = st.file_uploader("Choose an image...", type="jpg")

# Detect image with yolov8
def detect_image(uploaded_image):
    # Add yolov8 logic detection
    detected_objects = ["potato", "egg", "milk"]
    return detected_objects
