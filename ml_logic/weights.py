from comet_ml import API
from params import *

api = API(api_key=COMETML_APIKEY)

models = api.get_model(workspace='epicureai', model_name='yolov8_custom')
model = models.find_versions()[0]
models.download(version=model, output_folder='PATH', expand=True)
