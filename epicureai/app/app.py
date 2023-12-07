# app.py
import streamlit as st
import os
from style import load_styles
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import requests

# Configuration de la page et chargement des styles CSS
st.set_page_config(page_title="Epicure AI", layout="wide")
st.markdown(load_styles(), unsafe_allow_html=True)

# URL de l'API FastAPI
api_url = "https://epicureai-uky2zwgmvq-no.a.run.app"

### START OF UI HERE ###
st.title("Epicure AI")
st.write("Revolutionize your culinary experience with AI")

# Creating line breaks for spacing
st.markdown("<br>", unsafe_allow_html=True)


st.subheader('Select your dietary requirements...')

# Options pour le formulaire
diets = ["N/A", "Plant-based", "Vegetarian", "Pescatarian", "Gluten-Free", "Ketogenic", "Paleo", "Low-Carb", "Mediterranean", "Whole30", "DASH", "Low-FODMAP", "Flexitarian", "High-Protein"]
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


st.markdown("<br>", unsafe_allow_html=True)
st.subheader('Take a picture of your ingredients...')
#uploaded_image = st.file_uploader("Upload image...", type="jpg")
uploaded_image = st.camera_input('Camera')

def draw_yolo_annotations(image, annotations):
    draw = ImageDraw.Draw(image)

    # Utilisez soit une police système spécifique soit une police par défaut
    font_size = 30
    # Pour une police spécifique (ajustez le chemin)
    # font_path = "chemin/vers/la/police.ttf"
    # font = ImageFont.truetype(font_path, font_size)
    # Pour une police par défaut
    font = ImageFont.load_default().font_variant(size=font_size)

    for annotation in annotations:
        box = annotation['box']
        label = annotation['label']
        draw.rectangle(box, outline="red", width=2)
        text_position = (box[0], box[1] - font_size)
        draw.text(text_position, label, fill="white", font=font)

    return image


if uploaded_image is not None:
    # Diviser l'écran en deux colonnes
    col1, col2 = st.columns(2)

    # Colonne de gauche : Image originale
    with col1:
        st.markdown('#### My ingredients')
        original_image = Image.open(uploaded_image)
        st.image(original_image, caption="My ingredients", use_column_width=True)

    # Colonne de droite : Image avec annotations
    with col2:
        st.markdown('#### Detection by model')
        img_bytes = uploaded_image.getvalue()
        response = requests.post(api_url + "/upload_image", files={'file': img_bytes})
        response_json = response.json()

        # Vérifier si 'annotations' est présent dans la réponse
        if 'annotations' in response_json:
            annotated_image = draw_yolo_annotations(original_image.copy(), response_json['annotations'])
            st.image(annotated_image, caption="Ingredients detected", use_column_width=True)
        else:
            st.write("No annotations found")

    # En dessous des images : Afficher la recette
    if 'recipe' in response_json:
        recipe_text = response_json["recipe"]
        st.subheader("Epicure AI Recipe Suggestion:")
        st.write(recipe_text)
    else:
        st.write("No recipe found")
