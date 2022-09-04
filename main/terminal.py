from temperatur import aktuelleTemperatur
from humidity import aktuelleHumidity, dhtDevice
from level import aktuellerWasserstand
import time
from curses import *

zaehler = 0
anzahl = 200
pause = 1

def main(stdscr):

    while zaehler <= anzahl:
        try:
            messdaten_humidity = aktuelleHumidity()
            messdaten_temperatur = aktuelleTemperatur()
            messdaten_level = aktuellerWasserstand()

            stdscr.addstr(0, 0, "Der aktuelle Wasserstand beträgt: " + str(messdaten_level) + "cm bis zur Wasseroberfläche.")
            stdscr.addstr(3, 0, "Die aktuelle Temperatur beträgt: " + str(messdaten_temperatur) + "°C.")
            stdscr.addstr(6, 0, "DIe aktuelle Luftfeuchtigkeit beträgt: " + str(aktuelleHumidity) + "%.")

            time.sleep(pause)
            zaehler = zaehler + 1

        except RuntimeError as error:
            time.sleep(1.0)
            continue

        except Exception as error:
            dhtDevice.exit()
            raise error

        time.sleep(1.0)

    stdscr.getch()

wrapper(main)