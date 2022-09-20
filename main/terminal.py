from temperatur import aktuelleTemperatur
from humidity import aktuelleHumidity, dhtDevice
from level import aktuellerWasserstand
import time

zaehler = 0
anzahl = 1000000
pause = 1

while zaehler <= anzahl:
    try:
        messdaten_humidity = aktuelleHumidity()
        messdaten_temperatur = aktuelleTemperatur()
        messdaten_level = aktuellerWasserstand()

        text = "Der aktuelle Wasserstand beträgt: " + str(messdaten_level) + "cm bis zur Wasseroberfläche.\n" + "Die aktuelle Temperatur beträgt: " + str(messdaten_temperatur) + "°C.\n" + "DIe aktuelle Luftfeuchtigkeit beträgt: " + str(aktuelleHumidity) + "%."

        print(text, end="\r")

        time.sleep(pause)
        zaehler = zaehler + 1

    except RuntimeError as error:
        time.sleep(1.0)
        continue

    except Exception as error:
        dhtDevice.exit()
        raise error

    time.sleep(1.0)