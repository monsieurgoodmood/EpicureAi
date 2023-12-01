import streamlit as st
from PIL import Image
import os
import pandas as pd
from Project.api.functions import DIETS, detect_ingredients, ingredients_for_recipe, instructions_for_recipe

### START OF UI HERE ###
st.title("Epicure AI")
st.write("Revolutionize your culinary experience with AI")

# Creating line breaks for spacing
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.subheader('Select your dietary requirements')
# Select dietary needs
selected_diet = st.selectbox("Choose your diet", DIETS)
allergen_options = ["nuts", "dairy", "seafood"]
intolerance_options = ["lactose", "gluten", "soy"]
equipment_options = ["oven", "blender", "microwave"]
selected_allergies = st.multiselect("Select allergies", allergen_options)
selected_intolerances = st.multiselect("Select intolerances", intolerance_options)
selected_equipment = st.multiselect("Select kitchen equipment", equipment_options)

# Creating line breaks for spacing
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

# Upload image through Streamlit
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
    with col2:  # Change col1 to col2
        st.write('Detection by model')
        pred_image_path = os.path.join(os.getcwd(), 'prediction.jpg')
        st.image(Image.open(pred_image_path), caption="Detection by model", use_column_width=True, width=200)

    ### Implementing yolov8model for detection
    st.subheader("Epicure AI has detected the following ingredients:")
    ingredients_df = detect_ingredients(uploaded_image)
    st.dataframe(ingredients_df)

    # Suggest recipe with OpenAI
    st.subheader("Epicure AI recommends you the top 3 recipes to make:")

    # Create DataFrames
    recipe_ingredients_df = pd.DataFrame(ingredients_for_recipe())
    recipe_instructions_df = pd.DataFrame(instructions_for_recipe()).set_index('Recipe')

    # Iterate through recipes and display DataFrames
    for num, (recipe, ingredients, instructions) in enumerate(zip(recipe_ingredients_df['Recipe'], recipe_ingredients_df.iterrows(), recipe_instructions_df.iterrows()), start=1):
        st.write(f"Recipe {num}")

        # Display Ingredients DataFrame
        st.markdown("#### Ingredients")
        st.dataframe(ingredients[1].to_frame().T)  # Transpose to display as a row

        # Display Instructions DataFrame
        st.markdown("#### Instructions")
        st.text_area(f"Instructions for Recipe {num}", value=instructions[1]['Instructions'], height=200)

        st.markdown("---")  # Add a horizontal line between recipes for better separation
