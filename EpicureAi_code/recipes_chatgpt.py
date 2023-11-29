
from openai import OpenAI

def recipe_gpt(ingredients_list: list)-> str:
    client = OpenAI()
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "You are recipe assisstant that gives out recipes to the ingredients the user gives you "},
                {"role": "user", "content": " ,".join(ingredients_list)}]
    )
    return chat_completion.choices[0].message.content
