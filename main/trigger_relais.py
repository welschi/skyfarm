import datetime
import time

import RPi.GPIO as GPIO
pin = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(pin ,GPIO.OUT)

def uhrzeit2sec(uhrzeit):
    [h,m,s] = uhrzeit.split(":")
    return int(s) + 60*int(m) + 3600*int(h)

def set_relais_high():
    GPIO.output(pin, GPIO.HIGH)
    print("relais is on")

def set_relais_low():
    GPIO.output(pin, GPIO.LOW)
    print("relais is off")


currentTime = datetime.datetime.now()
i = currentTime.strftime("%H:%M:%S")

schalt_zeit = [
    uhrzeit2sec("11:00:00"),
    uhrzeit2sec("13:52:00"),
    uhrzeit2sec("13:59:00")
]

toleranz = 5 # sekunden
warte_zeit = 1

while True:
    currentTime = datetime.datetime.now()
    uhrzeit = currentTime.strftime("%H:%M:%S")
    print(uhrzeit)
    sec = uhrzeit2sec(uhrzeit)
    for s in schalt_zeit:
        diff = abs(sec - s)
        print(s, diff)
        if diff < toleranz:
            set_relais_high()
            time.sleep(5)
            set_relais_low()
            break
    time.sleep(warte_zeit)






