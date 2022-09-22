import time
import RPi.GPIO as GPIO

pin_relais = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin_relais,GPIO.OUT)

def trigger_relais():
    GPIO.output(pin_relais, GPIO.HIGH)
    timeout = 5  # [seconds]
    time.sleep(timeout)
    GPIO.output(pin_relais, GPIO.LOW)


trigger_relais()