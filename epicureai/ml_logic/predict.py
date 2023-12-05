from ultralytics import YOLO
from epicureai.params import *
import os
import cv2

uploaded_image = os.path.join(os.getcwd(),'epicureai','app','images','uploaded_image.jpg')

best_model = '/Users/arthurchoisnet/code/monsieurgoodmood/EpicureAi/best-113.pt'


def yolo_predict_ingedients(uploaded_image):
    model = YOLO(best_model)
    results = model.predict(uploaded_image, save=True, conf=0.4, imgsz=512)

    names = model.names

    ingredients = []
    for r in results:
        for c in r.boxes.cls:
            ingredients.append(names[int(c)])  # Ajoutez le nom de l'ingrédient en tant que string

    return ingredients
