from ultralytics import YOLO
from epicureai.params import *
import os

uploaded_image = '/Users/arthurchoisnet/code/monsieurgoodmood/EpicureAi/epicureai/app/uploaded_image_predict.jpeg'
print(uploaded_image)

best_model = '/Users/arthurchoisnet/code/monsieurgoodmood/EpicureAi/best-113.pt'


def yolo_predict_ingedients(uploaded_image):
    model = YOLO(best_model)
    results = model(uploaded_image)
    names = model.names

    ingredients = []
    for r in results:
        for c in r.boxes.cls:
            ingredients.append(names[int(c)])  # Ajoutez le nom de l'ingrédient en tant que string

    return ingredients
