from data.load.roboflow_load import load_data_from_roboflow
from ml_logic.train import train_model
from ml_logic.augmentation import augmentation_training_set, augmentation_validation_set
from params import *


def main():
    # load_data_from_roboflow()
    augmentation_training_set()
    augmentation_validation_set()
    # train_model(epochs=NUM_EPOCHS)

if __name__ == "__main__":
    main()