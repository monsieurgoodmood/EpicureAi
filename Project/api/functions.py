import pandas as pd
### FILE TO KEET ALL LOGICS ###


# Dietary requirements list
DIETS = [
        "", # Empty for no special needs
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


# Detect ingredients of uploaded image with yolov8
def detect_ingredients(uploaded_image):
    # Add yolov8 logic detection
    ingredients_data = {
    'Item Name': ['beef', 'rice', 'tomato', 'onion', 'carrot'],
    'Ingredients Count': [5, 8, 3, 6, 10]
    }

    df = pd.DataFrame(ingredients_data)
    df.set_index('Item Name', inplace=True)
    return df



# Ingredients DataFrame
import streamlit as st
import pandas as pd

# Function to create the Ingredients DataFrame
def ingredients_for_recipe():
    recipe_ingredients = {
        'Recipe': ['Recipe 1', 'Recipe 2', 'Recipe 3'],
        'Beef': [1, 1.5, 0.5],
        'Rice': [1, 1, 1],
        'Tomato': [1, 2, 1],
        'Onion': [1, 1, 1],
        'Carrot': [1, 2, 1],
        'Soy Sauce': [2, 0, 2],
        'Vegetable Oil': [1, 0, 1],
        'Beef Broth': [0, 1, 0],
        'Tomato Paste': [0, 1, 0],
        'Garlic': [0, 2, 0],
        'Eggs': [0, 0, 2],
        'Green Onions': [0, 0, 1]
    }
    return recipe_ingredients

# Function to create the Instructions DataFrame
def instructions_for_recipe():
    recipe_instructions = {
        'Recipe': ['Recipe 1', 'Recipe 2', 'Recipe 3'],
        'Instructions': [
            "1. Heat vegetable oil in a wok or skillet over medium-high heat.\n"
            "2. Add sliced beef and stir-fry until browned. Season with salt and pepper.\n"
            "3. Add sliced onion and julienned carrot. Cook until vegetables are tender-crisp.\n"
            "4. Stir in diced tomato and soy sauce. Cook for an additional 2-3 minutes.\n"
            "5. Serve the beef stir-fry over cooked rice.",

            "1. In a large pot, brown the stew meat over medium heat.\n"
            "2. Add diced onion and minced garlic. Cook until onion is translucent.\n"
            "3. Stir in chopped tomatoes, sliced carrots, beef broth, and tomato paste.\n"
            "4. Season with salt and pepper. Bring to a simmer, then reduce heat and cover.\n"
            "5. Let the stew simmer for 1-2 hours until the meat is tender.\n"
            "6. Serve the tomato and beef stew over cooked rice.",

            "1. Heat vegetable oil in a large pan or wok over medium-high heat.\n"
            "2. Add diced beef and cook until browned. Push the beef to the side of the pan.\n"
            "3. Add chopped onion and diced carrot. Cook until vegetables are tender.\n"
            "4. Push the vegetables to the side and pour beaten eggs into the pan. Scramble the eggs until cooked.\n"
            "5. Stir in cooked rice, diced tomato, and soy sauce. Mix well to combine.\n"
            "6. Cook for an additional 3-4 minutes until everything is heated through.\n"
            "7. Garnish with chopped green onions and serve."
        ]
    }
    return recipe_instructions
