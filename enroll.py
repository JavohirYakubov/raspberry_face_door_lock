#!/usr/bin/env python3

import cv2
import os
import re

def get_next_person_id():
    face_dir = "/home/devapp/Documents/projects/raspberry_face_id/dataset"
    max_id = 0
    if not os.path.exists(face_dir):
        os.makedirs(face_dir)
        return 1  # Start with ID 1 if the directory is just created

    # Regular expression to find IDs in filenames
    pattern = re.compile(r"User\.(\d+)\.\d+\.jpg")
    
    # Scan the directory for existing face images and determine the maximum ID used
    for filename in os.listdir(face_dir):
        match = pattern.match(filename)
        if match:
            id = int(match.group(1))
            if id > max_id:
                max_id = id

    return max_id + 1  # Return the next ID

def capture_faces(person_id):
    face_dir = "/home/devapp/Documents/projects/raspberry_face_id/dataset"
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    cap = cv2.VideoCapture(0)
    count = 0

    while True:
        ret, frame = cap.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            count += 1
            cv2.imwrite(f"{face_dir}/User.{person_id}.{count}.jpg", gray[y:y+h, x:x+w])
        cv2.imshow('image', frame)    

        k = cv2.waitKey(100) & 0xff  # Press 'ESC' for exiting video
        if k == 27:
            break
        elif count >= 30:  # Take 30 face sample and stop video
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    person_id = get_next_person_id()
    print(f"Capturing faces for User ID {person_id}")
    capture_faces(person_id)
