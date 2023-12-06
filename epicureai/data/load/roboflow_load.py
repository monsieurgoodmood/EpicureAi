from roboflow import Roboflow
from epicureai.params import *


def load_data_from_roboflow():
    rf = Roboflow(api_key=ROBOFLOW_APIKEY)
    project = rf.workspace("wagon").project("epicureai")
    dataset = project.version(16).download("yolov8", location=LOCAL_DATA_PATH)


data=os.path.join(LOCAL_DATA_PATH,"data.yaml"),
if __name__ == "__main__":
    load_data_from_roboflow()
