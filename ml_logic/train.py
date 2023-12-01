import comet_ml
from ultralytics import YOLO
import os
from params import *
import yaml

COMETML_APIKEY="7rjl1Zsakp1QfmEObqF7Df9Hr"
experiment = comet_ml.Experiment(
    api_key=COMETML_APIKEY,
    project_name="epicureai"
)

def train_model(epochs: int = 10, img_size: int = 512, verbose=True):
    comet_ml.init()

    yaml_path = os.path.join(BASE_DIRECTORY, "data.yaml")

    # Load the pre-trained model
    model = YOLO('yolov8n.yaml').load('yolov8n.pt')
    # Train the model
    model.train(
        data=yaml_path,
        epochs=NUM_EPOCHS,
        imgsz=img_size,
        save=True,
        name="yolov8_custom",
        verbose=verbose
    )
    # Export the model to ONNX format
    path = model.export()
    print('✅ finished with training and exported the model' )


if __name__ == "__main__":
    train_model()
