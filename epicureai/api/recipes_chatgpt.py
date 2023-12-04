import openai
from Project.params import OPENAI_KEY

def mock_yolo_model(image):
    # Simuler une détection d'ingrédients à partir d'une image
    return ["spaghetti", "oats", "courgette"]

def generate_recipe(ingredients, diet, allergies, intolerances, time_available_in_minutes, kitchen_equipment):
    openai.api_key = OPENAI_KEY

    # Construire le message de l'utilisateur
    user_message = f"I need a recipe that only uses the following ingredients: {', '.join(ingredients)}."
    user_message += " The user only has these ingredients available, along with basic spices like salt, pepper, garlic, and water."

    if diet:
        user_message += f" The dietary preference is {diet}."
    if allergies:
        user_message += f" Please exclude any {', '.join(allergies)}."
    if intolerances:
        user_message += f" Please exclude any {', '.join(intolerances)}."
    if time_available_in_minutes:
        user_message += f" The preparation time available is {time_available_in_minutes} minutes."
    if kitchen_equipment:
        user_message += f" Only {', '.join(kitchen_equipment)} are available for use."

    client = OpenAI(api_key=OPENAI_KEY)

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant designed to output recipes."},
            {"role": "user", "content": user_message}
        ]
    )

    message = response.choices[0].message.content
    if message:
        return message.strip()

    print("No valid response or content found.")  # Message de débogage si aucune réponse valide n'est trouvée
    return "Sorry, I couldn't generate a recipe."
