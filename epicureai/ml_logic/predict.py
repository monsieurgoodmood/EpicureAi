from ultralytics import YOLO
from epicureai.params import *
import os

uploaded_image = os.path.join(os.getcwd(),'epicureai','app','images','uploaded_image_predict.jpg')
print(uploaded_image)

best_model = os.path.join(os.getcwd(),'best-113.pt')

def yolo_predict_ingedients(uploaded_image):
    model = YOLO(best_model)
    results = model(uploaded_image)

    names = model.names

    ingredients = []
    for r in results:
        for c in r.boxes.cls:
            ingredients.append(names[int(c)])

    return ingredients
