import os
import cv2
import numpy as np
import random
import math
from epicureai.params import *



def flip_image(image, flipCode):
    return cv2.flip(image, flipCode)

# Fonction pour lire les annotations
def read_annotation(file_path):
    with open(file_path, 'r') as file:
        annotations = file.readlines()
    return annotations

def flip_annotations(annotations, image_width, image_height, flipCode):
    new_annotations = []
    for annotation in annotations:
        class_id, x_center, y_center, width, height = map(float, annotation.split())
        if flipCode == 1:  # Flip horizontal
            x_center = 1 - x_center
        elif flipCode == 0:  # Flip vertical
            y_center = 1 - y_center
        elif flipCode == -1:  # Flip both
            x_center = 1 - x_center
            y_center = 1 - y_center
        new_annotations.append(f"{class_id} {x_center} {y_center} {width} {height}\n")
    return new_annotations

def adjust_brightness(image, value):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(hsv)
    v = cv2.add(v, value)
    v[v > 255] = 255
    v[v < 0] = 0
    final_hsv = cv2.merge((h, s, v))
    return cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)


# Fonction pour écrire les nouvelles annotations
def write_annotation(new_file_path, annotations):
    with open(new_file_path, 'w') as file:
        for annotation in annotations:
            file.write(annotation)

def rotate_image(image, angle):
    height, width = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), angle, 1)
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
    return rotated_image

def adjust_annotations_for_rotation(annotations, image_width, image_height, angle):
    new_annotations = []
    # Convertir l'angle de degrés en radians pour la rotation
    angle_rad = math.radians(angle)

    for annotation in annotations:
        class_id, x_center, y_center, width, height = map(float, annotation.split())

        # Convertir les coordonnées du centre en pixels
        x_center = x_center * image_width
        y_center = y_center * image_height
        bbox_width = width * image_width
        bbox_height = height * image_height

        # Calculer l'angle de rotation en fonction de l'angle donné
        if angle == 90:
            x_center_new = y_center / image_height
            y_center_new = 1 - (x_center / image_width)
        elif angle == 180:
            x_center_new = 1 - (x_center / image_width)
            y_center_new = 1 - (y_center / image_height)
        elif angle == 270:
            x_center_new = 1 - (y_center / image_height)
            y_center_new = x_center / image_width
        else:
            x_center_new = x_center / image_width
            y_center_new = y_center / image_height

        # Pour une rotation de 90 ou 270 degrés, échangez la largeur et la hauteur de la boîte englobante
        if angle in [90, 270]:
            width_new = bbox_height / image_width
            height_new = bbox_width / image_height
        else:
            width_new = bbox_width / image_width
            height_new = bbox_height / image_height

        # Ajouter la nouvelle annotation à la liste
        new_annotations.append(f"{class_id} {x_center_new} {y_center_new} {width_new} {height_new}\n")

    return new_annotations

# Appliquer une transformation aléatoire à une image
def apply_random_transformation(image, annotations, transformation_type):
    if transformation_type == 'flip':
        flipCode = random.choice([-1, 0, 1])
        transformed_image = flip_image(image, flipCode)
        transformed_annotations = flip_annotations(annotations, image.shape[1], image.shape[0], flipCode)
    elif transformation_type == 'brightness':
        brightness_value = random.randint(-50, 50)
        transformed_image = adjust_brightness(image, brightness_value)
        transformed_annotations = annotations
    elif transformation_type == 'rotate':
        angle = random.choice([0, 90, 180, 270])  # Choix aléatoire d'angle
        transformed_image = rotate_image(image, angle)
        transformed_annotations = adjust_annotations_for_rotation(annotations, image.shape[1], image.shape[0], angle)
    return transformed_image, transformed_annotations

def process_images_annotations(images_directory, annotations_directory, new_base_directory, transformations_dict, subset_type):
    new_images_count = 0
    files = [f for f in os.listdir(images_directory) if f.endswith(".jpg")]
    random.shuffle(files)

    # Définition des chemins pour les sous-dossiers 'images' et 'labels'
    subset_images_directory = os.path.join(new_base_directory, subset_type, "images")
    subset_annotations_directory = os.path.join(new_base_directory, subset_type, "labels")
    os.makedirs(subset_images_directory, exist_ok=True)
    os.makedirs(subset_annotations_directory, exist_ok=True)

    for filename in files:
        file_path = os.path.join(images_directory, filename)
        annotation_path = os.path.join(annotations_directory, filename.replace('.jpg', '.txt'))
        image = cv2.imread(file_path)
        annotations = read_annotation(annotation_path)

        for transformation_type, num_times in transformations_dict.items():
            for _ in range(num_times):
                transformed_image, transformed_annotations = apply_random_transformation(image, annotations, transformation_type)

                # Utiliser les sous-dossiers pour enregistrer les fichiers transformés
                new_image_file = os.path.join(subset_images_directory, f"{transformation_type}_image_{new_images_count}.jpg")
                new_annotation_file = os.path.join(subset_annotations_directory, f"{transformation_type}_annotation_{new_images_count}.txt")

                cv2.imwrite(new_image_file, transformed_image)
                write_annotation(new_annotation_file, transformed_annotations)
                new_images_count += 1

# Dossiers pour le dataset original
base_directory = LOCAL_DATA_PATH

train_images_directory = os.path.join(base_directory, "train/images")
train_annotations_directory = os.path.join(base_directory, "train/labels")
validation_images_directory = os.path.join(base_directory, "valid/images")
validation_annotations_directory = os.path.join(base_directory, "valid/labels")

# Chemins pour le nouveau dataset
new_dataset_directory = "raw_data/new_dataset"
new_train_directory = os.path.join(new_dataset_directory, "train")
new_valid_directory = os.path.join(new_dataset_directory, "valid")

# Nombre d'images dans les ensembles d'entraînement et de validation (à mettre à jour)
num_train_images = 125  # Mettre à jour avec le nombre réel d'images d'entraînement
num_valid_images = 54   # Mettre à jour avec le nombre réel d'images de validation
total_images = num_train_images + num_valid_images
num_transformations = 5000  # Nombre total d'images transformées souhaitées
transformations_per_image = num_transformations // total_images

# Définir le nombre de fois que chaque transformation doit être appliquée
transformations_dict = {
    'flip': transformations_per_image // 3,
    'brightness': transformations_per_image // 3,
    'rotate': transformations_per_image // 3
}

def augmentation_training_set():
    # Appliquer les transformations sur l'ensemble d'entraînement
    return process_images_annotations(train_images_directory, train_annotations_directory, new_dataset_directory, transformations_dict, "train")

def augmentation_validation_set():
    # Ajuster les transformations pour l'ensemble de validation si nécessaire
    transformations_dict['flip'] += transformations_per_image % 3
    return process_images_annotations(validation_images_directory, validation_annotations_directory, new_dataset_directory, transformations_dict, "valid")
