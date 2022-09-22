from temperatur import aktuelleTemperatur
from humidity import aktuelleHumidity, dhtDevice
from level import aktuellerWasserstand
import time

import os

zaehler = 0
anzahl = 1000000
pause = 1


def printText(messdaten_level, messdaten_temperatur, messdaten_humidity):
    os.system("clear")
    text = f"""
    Der aktuelle Wasserstand beträgt: {messdaten_level} cm bis zur Wasseroberfläche.
    Die aktuelle Temperatur beträgt: {messdaten_temperatur} °C.
    Die aktuelle Luftfeuchtigkeit beträgt: {messdaten_humidity} %.
    """
    print(text)


while zaehler <= anzahl:
    try:
        messdaten_humidity = aktuelleHumidity()
        messdaten_temperatur = aktuelleTemperatur()
        messdaten_level = aktuellerWasserstand()
        printText(messdaten_level, messdaten_temperatur, messdaten_humidity)

        time.sleep(pause)
        zaehler = zaehler + 1

    except RuntimeError as error:
        print(error)
        time.sleep(pause)
        continue

    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(pause)