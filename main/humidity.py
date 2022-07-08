#######################################################################################################################
##  Importiere alle Bibs

import time
import board
import adafruit_dht

#######################################################################################################################
##  DHT22 Sensor mit GPIO Pin 26 gezeichnet

dhtDevice = adafruit_dht.DHT22(board.D26, use_pulseio=False)

#######################################################################################################################
##  Funktion zum Auslesen

def aktuelleHumidity():
    humidity = dhtDevice.humidity
    return humidity
