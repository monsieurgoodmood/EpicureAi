import os

# Model training
NUM_EPOCHS = 1
DEVICE = "cpu"
IMGSZ = 512

# Data augmentation
BASE_DIRECTORY = os.path.join(os.getcwd(), 'EpicureAi-12')

# Api key
ROBOFLOW_APIKEY = os.environ.get("ROBOFLOW_APIKEY")
COMETML_APIKEY = os.environ.get("COMETML_APIKEY")
