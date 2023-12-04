# app.py
import streamlit as st
from style import load_styles
from element import create_file_uploader, create_diet_selector, create_multiselect, create_time_slider, create_api_request
from PIL import Image
import os
import pandas as pd
from epicureai.api.recipes_chatgpt import mock_yolo_model, generate_recipe

# Configuration de la page et chargement des styles CSS
st.set_page_config(page_title="Epicure AI", layout="wide")
st.markdown(load_styles(), unsafe_allow_html=True)

# URL de l'API FastAPI
api_url = "https://epicureai.streamlit.app/"

### START OF UI HERE ###
st.title("Epicure AI")
st.write("Revolutionize your culinary experience with AI")

# Creating line breaks for spacing
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)


st.subheader('Select your dietary requirements...')

# Creating line breaks for spacing
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Options pour le formulaire
diets = ["", "Plant-based", "Vegetarian", "Pescatarian", "Gluten-Free", "Ketogenic", "Paleo", "Low-Carb", "Mediterranean", "Whole30", "DASH", "Low-FODMAP", "Flexitarian", "High-Protein"]
health_conditions_options = ["Diabetes", "High Cholesterol", "Hypertension", "Heart Disease", "Celiac Disease", "Kidney Disease", "Liver Disease"]
allergen_options = ["Peanuts", "Tree nuts", "Milk", "Eggs", "Fish", "Shellfish", "Molluscs", "Soy", "Gluten", "Sesame", "Mustard", "Celery", "Lupin", "Sulfites"]
intolerance_options = ["Lactose", "Gluten", "Fructose", "Histamine", "Caffeine", "Food Additives", "Salicylates", "Amines", "FODMAPs", "Sulfites", "Corn", "Yeast", "MSG"]
equipment_options = ["Oven", "Microwave", "Blender", "Food processor", "Toaster", "Kettle", "Deep fryer", "Stove", "Electric mixer", "Coffee machine", "Slow cooker", "Steamer", "Juicer", "Waffle iron", "Rice cooker", "Pressure cooker", "Grill", "Griddle", "Air fryer", "Panini press", "Induction cooktop", "Electric skillet"]

# Création des sélecteurs pour les préférences alimentaires et le matériel de cuisine
selected_diet = st.selectbox("Choose your diet", diets)
selected_health_conditions = st.multiselect("Select any health conditions", health_conditions_options)
selected_allergies = st.multiselect("Select allergies", allergen_options)
selected_intolerances = st.multiselect("Select intolerances", intolerance_options)
selected_equipment = st.multiselect("Select kitchen equipment", equipment_options)
time_available_in_minutes = st.slider("Time available for cooking (minutes)", min_value=15, max_value=120, value=30, step=5)

# Section de téléchargement d'image
st.subheader('Take a picture of your ingredients...')
uploaded_image = st.file_uploader("Upload image...", type="jpg")

# Save and display the uploaded image
if uploaded_image is not None:
    # Save the uploaded image
    image_path = os.path.join(os.getcwd(), "uploaded_image.jpg")
    with open(image_path, "wb") as f:
        f.write(uploaded_image.read())

    # Display the uploaded image
    col1, col2 = st.columns(2)
    with col1:
        st.write('My ingredients')
        st.image(Image.open(image_path), caption="My ingredients", use_column_width=True, width=200)
    with col2:
        st.write('Detection by model')
        pred_image_path = os.path.join(os.getcwd(), 'prediction.jpg')
        st.image(Image.open(pred_image_path), caption="Detection by model", use_column_width=True, width=200)

    st.subheader("Epicure AI has detected the following ingredients:")
    ingredients_df = mock_yolo_model(uploaded_image)
    st.dataframe(ingredients_df)

    ingredients = mock_yolo_model(uploaded_image)
    #st.write(", ".join(ingredients))

    # Générer la recette et afficher le résultat
    recipe_text = generate_recipe(ingredients, selected_diet, selected_allergies, selected_intolerances, time_available_in_minutes, selected_equipment)

    st.subheader("Epicure AI Recipe Suggestion:")
    st.write(recipe_text)
