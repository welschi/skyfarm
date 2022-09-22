import datetime
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

def trigger_relais():
    GPIO.output(pin_relais, GPIO.HIGH)
    timeout = 30  # [seconds]
    time.sleep(timeout)
    GPIO.output(pin_relais, GPIO.LOW)



if i == time1:  #and aqua_stop = false
    trigger_relais()
elif i == time2:  #and aqua_stop = false
    trigger_relais()
elif i == time3 :  #and aqua_stop = false
    trigger_relais()
else:
    GPIO.output(pin, GPIO.LOW)
