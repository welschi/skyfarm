#import schedule
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(5,GPIO.OUT)

def trigger_relais():
    timeout_start = time.time()
    timeout = 30  # [seconds]
    while time.time() < timeout_start + timeout:
        GPIO.output(5, GPIO.HIGH)



if time.strftime('%X') = '08:00:00' and aqua_stop = false:
    trigger_relais()
elif time.strftime('%X') = '15:00:00' and aqua_stop = false:
    trigger_relais()
elif time.strftime('%X') = '20:00:00' and aqua_stop = false:
    trigger_relais()
else:
    GPIO.output(5, GPIO.LOW)







