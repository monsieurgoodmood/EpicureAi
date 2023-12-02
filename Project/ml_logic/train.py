import comet_ml
from ultralytics import YOLO
import os
from Project.params import *
import yaml

experiment = comet_ml.Experiment(
    api_key=COMETML_APIKEY,
    project_name="epicureai"
)

def train_model(epochs: int = 10, img_size: int = 512, verbose=True):
    comet_ml.init()

    # Load the pre-trained model
    model = YOLO("yolov8n.pt")

    # Train the model
    model.train(
        data=YAML_PATH,
        epochs=NUM_EPOCHS,
        imgsz=img_size,
        save=True,
        device=DEVICE,
        name="yolov8_20_epochs",
        verbose=verbose
    )
    # Export the model to ONNX format
    path = model.export()
    print('✅ finished with training and exported the model' )


if __name__ == "__main__":
    train_model()