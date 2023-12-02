from roboflow import Roboflow
<<<<<<<< HEAD:Project/ml_logic/roboflow_load.py
from Project.params import *
========
from epicureai.params import *
>>>>>>>> API:epicureai/data/load/roboflow_load.py


def load_data_from_roboflow():
    rf = Roboflow(api_key=ROBOFLOW_APIKEY)
    project = rf.workspace("wagon").project("epicureai")
    dataset = project.version(12).download("yolov8")
    print('✅ loaded the dataset from roboflow')
    return dataset
