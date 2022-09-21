########################################################################################################################
## import alle Packages

import RPi.GPIO as GPIO
import time

########################################################################################################################
## Variablen festlegen

GPIO.setmode(GPIO.BCM)

TRIG = 14
ECHO = 15

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

########################################################################################################################
## Eigentlicher Auslese/Anzeigecode

GPIO.output(TRIG, False)
print("Starting.....")
time.sleep(2)

while True:
    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    # Start der Abstandsmessung
    while GPIO.input(ECHO) == 0:
        pulse_start = time.time()

    while GPIO.input(ECHO) == 1:
        pulse_stop = time.time()

    # Errechnen der gebrauchten Zeit
    pulse_time = pulse_stop - pulse_start

    # Errechnen des Abstandes
    distance = pulse_time * 17150

    if distance > detection_limit:
        aqua_stop = True
    else
        aqua_stop = False