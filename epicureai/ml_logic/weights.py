from comet_ml import API
<<<<<<<< HEAD:Project/ml_logic/weights.py
from Project.params import *
========
from epicureai.params import *
>>>>>>>> API:epicureai/ml_logic/weights.py

api = API(api_key=COMETML_APIKEY)

models = api.get_model(workspace='epicureai', model_name='yolov8')
model = models.find_versions()[0]
models.download(version=model, output_folder='PATH', expand=True)
