#######################################################################################################################
##  Importiere alle Bibs

import time
import board
import adafruit_dht

#######################################################################################################################
##  DHT22 Sensor mit GPIO Pin 26 gezeichnet

dhtDevice = adafruit_dht.DHT22(board.D26, use_pulseio=False)

#######################################################################################################################
##  Schleife zum Auslesen

while True:
    try:
        temp = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print("Temperatur: " + temp + " Hydro: " + humidity
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(2.0)
