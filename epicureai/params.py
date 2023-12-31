import os

LOCAL_DATA_PATH = os.path.expanduser("~/.epicureai_data")
MODEL_PATH = os.path.join(LOCAL_DATA_PATH, "models")
COMET_API_KEY = os.environ["COMET_API_KEY"]
COMET_PROJECT_NAME = os.environ["COMET_PROJECT_NAME"]
COMET_MODEL_NAME = os.environ["COMET_MODEL_NAME"]
COMET_WORKSPACE_NAME = os.environ["COMET_WORKSPACE_NAME"]
ROBOFLOW_APIKEY = os.environ["ROBOFLOW_APIKEY"]
NUM_EPOCHS = int(os.environ["NUM_EPOCHS"])
OPENAI_KEY = os.environ["OPENAI_KEY"]


os.makedirs(LOCAL_DATA_PATH, exist_ok=True)
os.makedirs(MODEL_PATH, exist_ok=True)
