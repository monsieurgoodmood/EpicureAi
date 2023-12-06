import requests
import random
from pathlib import Path
import json

url = "http://localhost:8000/upload_image"
# Chemin vers l'image
image_path = Path("/Users/arthurchoisnet/code/monsieurgoodmood/EpicureAi/epicureai/app/images/uploaded_image.jpg")

# Listes des valeurs possibles pour chaque paramètre
diets = ["vegetarian", "vegan", "gluten-free", None]
allergens = ["nuts", "dairy", "seafood", None]
intolerances = ["lactose", "gluten", "soy", None]
times = [15, 30, 45, 60]
equipments = ["oven", "blender", "microwave", None]

# Génération aléatoire de valeurs
diet = random.choice(diets)
allergies = [allergen for allergen in random.sample(allergens, k=random.randint(0, len(allergens))) if allergen is not None]
intolerances = [intolerance for intolerance in random.sample(intolerances, k=random.randint(0, len(intolerances))) if intolerance is not None]
time_available_in_minutes = random.choice(times)
kitchen_equipment = [equipment for equipment in random.sample(equipments, k=random.randint(0, len(equipments))) if equipment is not None]

# Préparation de la requête
multipart_form_data = {
    "file": (image_path.name, open(image_path, "rb"), "image/jpeg"),
    "diet": (None, diet),
    "time_available": (None, str(time_available_in_minutes)),
}

# Ajouter chaque allergie, intolérance et équipement comme un champ distinct
for i, allergy in enumerate(allergies):
    multipart_form_data[f"allergies[{i}]"] = (None, allergy)
for i, intolerance in enumerate(intolerances):
    multipart_form_data[f"intolerances[{i}]"] = (None, intolerance)
for i, equipment in enumerate(kitchen_equipment):
    multipart_form_data[f"kitchen_equipment[{i}]"] = (None, equipment)

response = requests.post(url, files=multipart_form_data)

if response.status_code == 200:
    try:
        response_json = response.json()
        print("Generated Recipe:", response_json['recipe'])
    except json.decoder.JSONDecodeError:
        print("Erreur de décodage JSON.")
else:
    print(f"La requête POST a échoué avec le statut : {response.status_code}")
    print(f"Réponse : {response.text}")
