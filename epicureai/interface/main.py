from epicureai.data.load.roboflow_load import load_data_from_roboflow
from epicureai.ml_logic.train import train_model
from epicureai.ml_logic.augmentation import augmentation_training_set, augmentation_validation_set
from epicureai.ml_logic.data_yaml import create_data_yaml
from epicureai.params import *
<<<<<<< HEAD

def main():
    load_data_from_roboflow()
    # Need to update the paths to our data in data.yaml
    augmentation_training_set()
    print('✅ done with augmenting training set')
    augmentation_validation_set()
    print('✅ done with augmenting validation set')
    #train_model(epochs=NUM_EPOCHS)
=======


def main():
    # load_data_from_roboflow()
    # augmentation_training_set()
    # print('✅ done with augmenting training set')
    # augmentation_validation_set()
    # print('✅ done with augmenting validation set')
    # create_data_yaml()
    # print('✅ data.yaml with augmented images created')
    train_model(epochs=NUM_EPOCHS)
>>>>>>> 2954507dc570f6fc03fb468a1a77bfc5c2397e01

if __name__ == "__main__":
    main()
