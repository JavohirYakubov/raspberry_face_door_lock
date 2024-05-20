#!/usr/bin/env python3
# Javohir Yakubov
import cv2
import numpy as np
import RPi.GPIO as GPIO
import time
import threading
import os

global ON
global OFF
ON = GPIO.LOW
OFF = GPIO.HIGH

# GPIO Pin setup
relay_pin = 27  # Change this to the GPIO pin you're using
GPIO.cleanup()
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)

def turn_off_relay():
    GPIO.output(relay_pin, OFF)
    print("Relay turned off.")


def recognize():
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    face_recognizer = cv2.face.LBPHFaceRecognizer_create()
    face_recognizer.read("/home/devapp/Documents/projects/raspberry_face_id/trainer.yml")
    cap = cv2.VideoCapture(0)
    GPIO.output(relay_pin, OFF)

    relay_active = False
    last_activation_time = 0
    relay_duration = 5  # Relay on for 5 seconds

    try:
        while True:
            ret, frame = cap.read()
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, 1.3, 5)

            for (x, y, w, h) in faces:
                roi_gray = gray[y:y+h, x:x+w]
                label, confidence = face_recognizer.predict(roi_gray)

                if confidence > 85 and not relay_active:
                    relay_active = True
                    GPIO.output(relay_pin, ON)
                    print(f"Face detected with confidence {confidence}. Turning on the relay.")
                    # Schedule relay to turn off after 5 seconds
                    threading.Timer(relay_duration, turn_off_relay).start()
                    last_activation_time = time.time()

                print(f"Label: {label}, Aniqlilik: {confidence}")
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, f"Label: {label}, Aniqlilik: {confidence}", (x+5, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            # Check if it's time to reactivate the relay
            if relay_active and (time.time() - last_activation_time > relay_duration):
                relay_active = False

    finally:
        cap.release()
        cv2.destroyAllWindows()
        GPIO.cleanup()

if __name__ == "__main__":
    recognize()
