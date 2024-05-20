#!/usr/bin/env python3

import cv2
import os
import numpy as np

def train_recognizer():
    face_dir = "/home/devapp/Documents/projects/raspberry_face_id/dataset"
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    print("\n [INFO] Training faces. It will take a few seconds. Wait ...")
    faces, labels = [], []

    for file_name in os.listdir(face_dir):
        if file_name.startswith("User"):
            label = int(file_name.split('.')[1])
            image_path = os.path.join(face_dir, file_name)
            image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
            faces.append(image)
            labels.append(label)

    face_recognizer.train(faces, np.array(labels))
    face_recognizer.save('/home/devapp/Documents/projects/raspberry_face_id/trainer.yml')
    print("Training complete, model saved as 'trainer.yml'")

if __name__ == "__main__":
    train_recognizer()
