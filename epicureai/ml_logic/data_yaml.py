import os
import yaml
from epicureai.params import *

def create_data_yaml():
    data = {
        'names': [
            'almond_milk', 'avocado', 'banana', 'carrot', 'courgette',
            'cured_goat_cheese', 'egg', 'milk', 'oat_milk', 'oats',
            'olive_oil', 'potato', 'quinoa', 'rice', 'salmon', 'spaghetti',
            'sweet_potato', 'tomato'
        ],
        'nc': 18,
        'train': 'train/images',
        'val': 'valid/images'
    }

    # Define the path to the data.yaml file inside the augmented_data folder
    file_path = os.path.join(LOCAL_DATA_PATH, 'augmented_data', 'data.yaml')

    with open(file_path, 'w') as yaml_file:
        yaml.dump(data, yaml_file, default_flow_style=False)

    print(f"Created {file_path}")
