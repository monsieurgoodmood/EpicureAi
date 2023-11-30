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


diets = [
    "",  # Option pour aucun régime spécifique
    "Vegetarian",
    "Vegan",
    "Pescatarian",
    "Gluten-Free",
    "Ketogenic",
    "Paleo",
    "Low-Carb",
    "Mediterranean",
    "Whole30",
    "DASH",
    "Low-FODMAP",
    "Flexitarian",
    "High-Protein"
]

# oneselect optionnal box
selected_diet = st.selectbox("Choose your diet", diets)


allergen_options = ["nuts", "dairy", "seafood"]
intolerance_options = ["lactose", "gluten", "soy"]
equipment_options = ["oven", "blender", "microwave"]

selected_allergies = st.multiselect("Select allergies", allergen_options)
selected_intolerances = st.multiselect("Select intolerances", intolerance_options)
selected_equipment = st.multiselect("Select kitchen equipment", equipment_options)

# Les variables selected_allergies, selected_intolerances et selected_equipment
# contiendront les choix de l'utilisateur sous forme de listes.


# Et ainsi de suite pour les autres paramètres...
