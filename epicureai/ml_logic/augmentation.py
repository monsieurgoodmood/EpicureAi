from epicureai.params import *
import os
import cv2
import random
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import shutil
import yaml

def flip_image(image, flipCode):
    return cv2.flip(image, flipCode)

def read_annotation(file_path):
    with open(file_path, 'r') as file:
        annotations = file.readlines()
    return annotations

def flip_annotations(annotations, image_width, image_height, flipCode):
    new_annotations = []
    for annotation in annotations:
        class_id, x_center, y_center, width, height = map(float, annotation.split())
        if flipCode == 1:
            x_center = 1 - x_center
        elif flipCode == 0:
            y_center = 1 - y_center
        elif flipCode == -1:
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
    angle_rad = math.radians(angle)

    for annotation in annotations:
        class_id, x_center, y_center, width, height = map(float, annotation.split())

        x_center = x_center * image_width
        y_center = y_center * image_height
        bbox_width = width * image_width
        bbox_height = height * image_height

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

        if angle in [90, 270]:
            width_new = bbox_height / image_width
            height_new = bbox_width / image_height
        else:
            width_new = bbox_width / image_width
            height_new = bbox_height / image_height

        new_annotations.append(f"{class_id} {x_center_new} {y_center_new} {width_new} {height_new}\n")

    return new_annotations

def replace_background(image, annotations, new_background_color):
    mask = np.zeros(image.shape[:2], dtype="uint8")

    for annotation in annotations:
        class_id, x_center, y_center, width, height = map(float, annotation.split())
        x_center, y_center, width, height = (x_center * image.shape[1], y_center * image.shape[0],
                                             width * image.shape[1], height * image.shape[0])
        top_left = (int(x_center - width / 2), int(y_center - height / 2))
        bottom_right = (int(x_center + width / 2), int(y_center + height / 2))
        cv2.rectangle(mask, top_left, bottom_right, 255, -1)

    background_mask = cv2.bitwise_not(mask)
    background = np.full(image.shape, new_background_color, dtype="uint8")
    foreground = cv2.bitwise_and(image, image, mask=mask)
    new_background = cv2.bitwise_and(background, background, mask=background_mask)
    result = cv2.add(foreground, new_background)
    return result

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
        angle = random.choice([0, 90, 180, 270])
        transformed_image = rotate_image(image, angle)
        transformed_annotations = adjust_annotations_for_rotation(annotations, image.shape[1], image.shape[0], angle)
    elif transformation_type == 'background':
        for _ in range(10):  # Generate 10 different backgrounds
            background_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            transformed_image = replace_background(image, annotations, background_color)
            transformed_annotations = annotations  # Background change does not affect annotations
    return transformed_image, transformed_annotations

def process_images_annotations(images_directory, annotations_directory, new_base_directory, transformations_dict, subset_type):
    new_images_count = 0
    files = [f for f in os.listdir(images_directory) if f.endswith(".jpg")]
    random.shuffle(files)

    subset_images_directory = os.path.join(new_base_directory, subset_type, "images")
    subset_annotations_directory = os.path.join(new_base_directory, subset_type, "labels")
    os.makedirs(subset_images_directory, exist_ok=True)
    os.makedirs(subset_annotations_directory, exist_ok=True)

    # Copier les images et annotations originales
    for filename in files:
        original_image_path = os.path.join(images_directory, filename)
        original_annotation_path = os.path.join(annotations_directory, filename.replace('.jpg', '.txt'))
        shutil.copy(original_image_path, subset_images_directory)
        shutil.copy(original_annotation_path, subset_annotations_directory)

    # Appliquer les transformations
    for filename in files:
        file_path = os.path.join(images_directory, filename)
        annotation_path = os.path.join(annotations_directory, filename.replace('.jpg', '.txt'))
        image = cv2.imread(file_path)
        annotations = read_annotation(annotation_path)

        for transformation_type, num_times in transformations_dict.items():
            for _ in range(num_times):
                transformed_image, transformed_annotations = apply_random_transformation(image, annotations, transformation_type)

                new_image_file = os.path.join(subset_images_directory, f"{transformation_type}_image_{new_images_count}.jpg")
                new_annotation_file = os.path.join(subset_annotations_directory, f"{transformation_type}_annotation_{new_images_count}.txt")

                cv2.imwrite(new_image_file, transformed_image)
                write_annotation(new_annotation_file, transformed_annotations)
                new_images_count += 1


# Configuration des chemins
base_directory = LOCAL_DATA_PATH
train_images_directory = os.path.join(base_directory, "train/images")
train_annotations_directory = os.path.join(base_directory, "train/labels")
validation_images_directory = os.path.join(base_directory, "valid/images")
validation_annotations_directory = os.path.join(base_directory, "valid/labels")

# new_dataset_directory = "raw_data/new_dataset_transformed"
new_dataset_directory = os.path.join(LOCAL_DATA_PATH, 'augmented_data')
os.makedirs(new_dataset_directory, exist_ok=True)
new_train_directory = os.path.join(new_dataset_directory, "train")
new_valid_directory = os.path.join(new_dataset_directory, "valid")

num_train_images = 253
num_valid_images = 110
total_images = num_train_images + num_valid_images
num_transformations = 5000
transformations_per_image = num_transformations // total_images

transformations_dict = {
    'flip': transformations_per_image // 4,
    'brightness': transformations_per_image // 4,
    'rotate': transformations_per_image // 4,
    'background': 10  # Ajouter 10 variations d'arrière-plan pour chaque image
}

def augmentation_training_set():
    # Appliquer les transformations sur l'ensemble d'entraînement
    return process_images_annotations(train_images_directory, train_annotations_directory, new_dataset_directory, transformations_dict, "train")

def augmentation_validation_set():
    # Ajuster les transformations pour l'ensemble de validation si nécessaire
    transformations_dict['flip'] += transformations_per_image % 4
    return process_images_annotations(validation_images_directory, validation_annotations_directory, new_dataset_directory, transformations_dict, "valid")
