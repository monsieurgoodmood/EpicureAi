<<<<<<< HEAD
from comet_ml import API
from epicureai.params import *

api = API(api_key=COMETML_APIKEY)

models = api.get_model(workspace='epicureai', model_name='yolov8')
model = models.find_versions()[0]
models.download(version=model, output_folder='PATH', expand=True)
=======
#from comet_ml import API
#
#from Project.params import *
#
#from epicureai.params import *
#
#
#api = API(api_key=COMETML_APIKEY)
#
#models = api.get_model(workspace='epicureai', model_name='yolov8')
#model = models.find_versions()[0]
#models.download(version=model, output_folder='PATH', expand=True)
>>>>>>> f425289b4762e60603d7259af00a20a70b58ad74
