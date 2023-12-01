import os

# Model training
NUM_EPOCHS = 10
<<<<<<< HEAD
DEVICE = "cpu"
=======
DEVICE = "gpu"
>>>>>>> dc72aa5c011ce0186812a99cc18e247d34217a41
IMGSZ = 512

# Comet ML
WEIGHTS = os.path.join(os.getcwd(),'comet_ml')

# Data Augmentation
BASE_DIRECTORY = os.path.join(os.getcwd(), 'EpicureAi-12')
YAML_PATH = os.path.join(BASE_DIRECTORY,'data.yaml')

# API Key
ROBOFLOW_APIKEY = os.environ.get("ROBOFLOW_APIKEY")
COMETML_APIKEY = os.environ.get("COMETML_APIKEY")
OPENAI_KEY = os.environ.get("OPENAI_KEY")
