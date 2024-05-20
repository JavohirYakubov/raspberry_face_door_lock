import RPi.GPIO as GPIO
import time

relay_pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(relay_pin, GPIO.OUT)


try:
    while True:
        try:
            print("Turning on the relay.")
            GPIO.output(relay_pin, GPIO.HIGH)
            time.sleep(5)
            print("Turning off the relay.")
            GPIO.output(relay_pin, GPIO.LOW)
            time.sleep(1)
        except Exception as e:
            print(f"An error occurred: {e}")
            break  # Optionally break the loop if an error occurs
finally:
    GPIO.cleanup()