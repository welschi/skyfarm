import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.OUT)

def trigger_relais():
    GPIO.setup(5, GPIO.HIGH)
    timeout = 90  # [seconds]
    time.sleep(timeout)
    GPIO.setup(5, GPIO.LOW)


trigger_relais()