from ultralytics import YOLO
from epicureai.params import *
import os

#uploaded_image = os.path.join(os.getcwd(),'epicureai','app','images','uploaded_image.jpg')



#pqath = os.path.join(LOCAL_DATA_PATH,'models', 'best-113.pt')

def yolo_predict_ingedients(uploaded_image):
    best_model = os.path.join(MODEL_PATH, 'best-113.pt')
    model = YOLO(best_model)
    results = model.predict(uploaded_image, save=True, conf=0.4, imgsz=512)

    names = model.names
    ingredients = []
    annotations = []

    for r in results:
        for box, label in zip(r.boxes.xywh.tolist(), r.boxes.cls.tolist()):  # Conversion en liste
                # Calcul des coordonnées de la boîte englobante
            x_center, y_center, width, height = box
            x0 = x_center - width / 2
            y0 = y_center - height / 2
            x1 = x_center + width / 2
            y1 = y_center + height / 2

            annotations.append({
                'box': [x0, y0, x1, y1],
                'label': names[int(label)]
            })
            ingredients.append(names[int(label)])

    return ingredients, annotations
