
import openai

#def recipe_gpt(ingredients_list: list)-> str:
#   client = OpenAI()
#    chat_completion = client.chat.completions.create(
#        model="gpt-3.5-turbo",
#       messages=[{"role": "system", "content": "You are recipe assisstant that gives out recipes to the ingredients the user gives you "},
#               {"role": "user", "content": " ,".join(ingredients_list)}]
#    )
#    return chat_completion.choices[0].message.content

def mock_yolo_model(image):
    # Simulez une détection d'ingrédients à partir d'une image
    return ["spaghetti", "oats", "courgette"]

def generate_recipe(ingredients, diet, allergies, intolerances, time_available, kitchen_equipment):
    openai.api_key = "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"

    # Construire le prompt avec les informations de l'utilisateur
    prompt = f"Create a detailed recipe using these ingredients: {', '.join(ingredients)}"
    if diet:
        prompt += f", dietary preference: {diet}"
    if allergies:
        prompt += f", excluding {', '.join(allergies)}"
    if intolerances:
        prompt += f", excluding {', '.join(intolerances)}"
    if time_available:
        prompt += f", preparation time: {time_available} minutes"
    if kitchen_equipment:
        prompt += f", available equipment: {', '.join(kitchen_equipment)}"
    prompt += "."

    # Calculer le nombre de tokens
    base_tokens = 100  # Nombre de base de tokens pour une recette simple
    additional_tokens_per_ingredient = 5  # Tokens supplémentaires par ingrédient
    max_tokens = 300  # Limite maximale de tokens pour éviter des coûts excessifs

    total_tokens = min(base_tokens + additional_tokens_per_ingredient * len(ingredients), max_tokens)

    # Appel à l'API OpenAI
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=total_tokens
    )

    return response.choices[0].text.strip()
