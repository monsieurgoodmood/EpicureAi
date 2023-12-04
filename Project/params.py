import os

# Model training
NUM_EPOCHS = 10
DEVICE = "gpu"
IMGSZ = 512

# Comet ML
WEIGHTS = os.path.join(os.getcwd(),'comet_ml')

# Data Augmentation
PROJECT_DIR = os.path.join(os.getcwd(), 'Project')
BASE_IMAGES_DIR = os.path.join(PROJECT_DIR, 'EpicureAi-12')
AUGMENTED_IMAGES_DIR = os.path.join(PROJECT_DIR,'augmented_data')
YAML_PATH = os.path.join(BASE_IMAGES_DIR,'data.yaml')

# API Key
ROBOFLOW_APIKEY = os.environ.get("ROBOFLOW_APIKEY")
COMETML_APIKEY = os.environ.get("COMETML_APIKEY")
OPENAI_KEY = os.environ.get("OPENAI_KEY")
