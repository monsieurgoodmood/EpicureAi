from epicureai.data.load.roboflow_load import load_data_from_roboflow
<<<<<<< HEAD
from ml_logic.train import train_model
from ml_logic.augmentation import augmentation_training_set, augmentation_validation_set
from epicureai.params import *

=======
from epicureai.ml_logic.train import train_model
from epicureai.ml_logic.augmentation import augmentation_training_set, augmentation_validation_set
from epicureai.params import *
>>>>>>> f425289b4762e60603d7259af00a20a70b58ad74

def main():
    load_data_from_roboflow()
    # Need to update the paths to our data in data.yaml
    #augmentation_training_set()
    #print('✅ done with augmenting training set')
    #augmentation_validation_set()
    #print('✅ done with augmenting validation set')
    train_model(epochs=NUM_EPOCHS)

if __name__ == "__main__":
    main()
