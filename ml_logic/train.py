from ultralytics import YOLO
import comet_ml
import os
from params import *

def train_model(epochs: int = 10, img_size: int = 512):
    comet_ml.init()
    yaml_path = os.path.join(
        os.path.expanduser("~"), ".lewagon", "data", "roboflow", "data.yaml"
    )
    # Load the pre-trained model
    model = YOLO("yolov8n.pt")

    # Train the model
    model.train(
        data=yaml_path,
        epochs=NUM_EPOCHS,
        imgsz=img_size,
        save=True,
        device=DEVICE,
    )
    # Export the model to ONNX format
    path = model.export()
    print('✅ finished with training and exported the model' )


if __name__ == "__main__":
    train_model()
