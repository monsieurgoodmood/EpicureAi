from roboflow import Roboflow
from Project.params import *



def load_data_from_roboflow():
    rf = Roboflow(api_key=ROBOFLOW_APIKEY)
    project = rf.workspace("wagon").project("epicureai")
    dataset = project.version(12).download("yolov8")
    print('✅ loaded the dataset from roboflow')
    return dataset
