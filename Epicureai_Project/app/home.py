import streamlit as st
from PIL import Image
import requests


st.title("Epicure AI")
st.write("Revolutionize your culinary experience with AI")


# Upload image through Streamlit
uploaded_image = st.file_uploader("Choose an image...", type="jpg")

# Detect image with yolov8
def detect_ingredients(uploaded_image):
    # Add yolov8 logic detection
    ingredients_list = ["potato", "egg", "milk"]
    return ingredients_list
