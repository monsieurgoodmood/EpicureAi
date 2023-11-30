import comet_ml
from ultralytics import YOLO
import os
from params import *

experiment = comet_ml.Experiment(
    api_key=COMETML_APIKEY,
    project_name="epicureai"
)

def train_model(epochs: int = 10, img_size: int = 512, verbose=True):
    comet_ml.init()

    yaml_path = os.path.join(BASE_DIRECTORY, "data.yaml")
    # Load the pre-trained model
    model = YOLO("yolov8n.pt")

    # Train the model
    model.train(
        data=yaml_path,
        epochs=NUM_EPOCHS,
        imgsz=img_size,
        save=True,
        device=DEVICE,
        verbose=verbose
    )

    # Inside your training loop or after model training
    training_metrics = model.results["train"]["metrics"]
    validation_metrics = model.results["val"]["metrics"]

    # Log metrics to Comet.ml
    experiment.log_metrics({
        "training_loss": training_metrics["total_loss"],
        "validation_loss": validation_metrics["total_loss"],
        "mAP": validation_metrics["mAP"],
        "precision": validation_metrics["precision"],
        "iou": validation_metrics["P_bbox"],
    })

    # Export the model to ONNX format
    path = model.export()
