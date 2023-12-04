import os

# Model training
<<<<<<< HEAD
NUM_EPOCHS = 10
<<<<<<< HEAD
=======
NUM_EPOCHS = 20
>>>>>>> api-streamlit
DEVICE = "cpu"
=======
DEVICE = "gpu"
>>>>>>> dc72aa5c011ce0186812a99cc18e247d34217a41
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
