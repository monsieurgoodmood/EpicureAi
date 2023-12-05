from ultralytics import YOLO
from epicureai.params import *

uploaded_image = '/Users/joaqo/code/joaquin-ortega84/projects/EpicureAi/epicureai/app/prediction.jpg'

def yolo_predict(uploaded_image):
    # Load the YOLOv8 model
    model = YOLO('/Users/joaqo/code/joaquin-ortega84/projects/EpicureAi/yolov8n.pt')

    # Make predictions on the uploaded image
    results = model(uploaded_image)

    # Print or return the results as needed
    print(results)
    return results

yolo_predict(uploaded_image)
