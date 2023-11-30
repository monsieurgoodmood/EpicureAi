import requests
import random
from pathlib import Path
import json

url = "http://localhost:8000/upload_image"
# Chemin vers l'image
image_path = Path("/Users/arthurchoisnet/code/monsieurgoodmood/EpicureAi/raw_data/new_dataset/train/images/brightness_image_4.jpg")

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
time_available = random.choice(times)
kitchen_equipment = [equipment for equipment in random.sample(equipments, k=random.randint(0, len(equipments))) if equipment is not None]

# Préparation de la requête
multipart_form_data = {
    "file": (image_path.name, open(image_path, "rb"), "image/jpeg"),
    "diet": (None, diet),
    "time_available": (None, str(time_available)),
}

# Ajouter chaque allergie, intolérance et équipement comme un champ distinct
for i, allergy in enumerate(allergies):
    multipart_form_data[f"allergies[{i}]"] = (None, allergy)
for i, intolerance in enumerate(intolerances):
    multipart_form_data[f"intolerances[{i}]"] = (None, intolerance)
for i, equipment in enumerate(kitchen_equipment):
    multipart_form_data[f"kitchen_equipment[{i}]"] = (None, equipment)

# Envoi de la requête POST
response = requests.post(url, files=multipart_form_data)

# Afficher le code de statut et le texte de la réponse
print("Status Code:", response.status_code)
print("Response Text:", response.text)

# Tentative de décodage JSON seulement si la réponse est 200 OK
if response.status_code == 200:
    try:
        print("JSON Response:", response.json())
    except json.decoder.JSONDecodeError:
        print("Erreur de décodage JSON.")
else:
    print("La requête POST a échoué.")
