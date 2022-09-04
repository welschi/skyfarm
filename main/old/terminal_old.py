#!/usr/bin/env python

from temperatur import aktuelleTemperatur
from humidity import aktuelleHumidity, dhtDevice
from level import aktuellerWasserstand
import time

schleifenZaehler = 0
schleifenAnzahl = 20
schleifenPause = 1

print("Luftfeuchtigkeits-, Temperatur- und Füllstandabfrage für ", schleifenAnzahl, " Messungen alle ", schleifenPause, " Sekunden gestartet.", "\n")

while schleifenZaehler <= schleifenAnzahl:
    try:
        messdaten_humidity = aktuelleHumidity()
        messdaten_temperatur = aktuelleTemperatur()
        messdaten_level = aktuellerWasserstand()
        print('Aktuelle Luftfeuchtigkeit [%] : ', messdaten_humidity, "\n", "Aktuelle Temperatur [°C] : ", messdaten_temperatur, "\n", "Aktueller Wasserstand [cm] : ", messdaten_level, "\n", "in der ", schleifenZaehler, ". Messabfrage", "\n")
        time.sleep(schleifenPause)
        schleifenZaehler = schleifenZaehler + 1

    except RuntimeError as error:
        print("Beim nächsten Mal wirds besser")
        time.sleep(1.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(1.0)

print("Messungen beendet.")

