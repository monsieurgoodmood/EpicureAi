from roboflow import Roboflow
from epicureai.params import *


def load_data_from_roboflow():
    rf = Roboflow(api_key=ROBOFLOW_APIKEY)
    project = rf.workspace("wagon").project("epicureai")
    dataset = project.version(13).download("yolov8", location=LOCAL_DATA_PATH)


if __name__ == "__main__":
    load_data_from_roboflow()
