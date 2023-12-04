import os

# Model training
DEVICE = "gpu"
NUM_EPOCHS = 10
IMGSZ = 512

# Comet ML
WEIGHTS = os.path.join(os.getcwd(),'comet_ml')

# Data Augmentation
BASE_DIRECTORY = os.path.join(os.getcwd(), 'EpicureAi.v12-balanced_data_set.yolov8')
YAML_PATH = os.path.join(BASE_DIRECTORY,'data.yaml')

# API Key
ROBOFLOW_APIKEY = os.environ.get("ROBOFLOW_APIKEY")
COMETML_APIKEY = os.environ.get("COMETML_APIKEY")
OPENAI_KEY = os.environ.get("OPENAI_KEY")
LOCAL_DATA_PATH = os.path.expanduser("~/.epicureai_data")
NUM_EPOCHS = int(os.environ["NUM_EPOCHS"])
COMET_API_KEY = os.environ["COMET_API_KEY"]
COMET_PROJECT_NAME = os.environ["COMET_PROJECT_NAME"]
COMET_MODEL_NAME = os.environ["COMET_MODEL_NAME"]
COMET_WORKSPACE_NAME = os.environ["COMET_WORKSPACE_NAME"]
