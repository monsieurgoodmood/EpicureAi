# elements.py
import streamlit as st

def create_file_uploader():
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
    return uploaded_file

def create_diet_selector(diets):
    selected_diet = st.selectbox("Choose your diet", diets)
    return selected_diet

def create_multiselect(title, options):
    selection = st.multiselect(f"Select {title}", options)
    return selection

def create_time_slider():
    time_available = st.slider("Time available for cooking (minutes)", min_value=15, max_value=120, value=30, step=5)
    return time_available

def create_api_request(uploaded_file, api_url):
    if uploaded_file is not None:
        files = {"file": uploaded_file.getvalue()}
        response = st.session_state['requests'].post(api_url, files=files)
        return response
