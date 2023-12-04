from roboflow import Roboflow
from epicureai.params import *


def load_data_from_roboflow():
    rf = Roboflow(api_key="Y3lBMUN1R4cIQVX0YLpO")
    project = rf.workspace("wagon").project("epicureai")
    dataset = project.version(12).download("yolov8", location=LOCAL_DATA_PATH)


if __name__ == "__main__":
    load_data_from_roboflow()
