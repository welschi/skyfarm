from temperatur import aktuelleTemperatur
import time

schleifenZaehler = 0
schleifenAnzahl = 20
schleifenPause = 1

print("Temperaturabfrage für ", schleifenAnzahl, " Messungen alle ", schleifenPause, " Sekunden gestartet")

while schleifenZaehler <= schleifenAnzahl:
    messdaten = aktuelleTemperatur()
    print("Aktuelle Temperatur : ", messdaten, "°C, in der ", schleifenZaehler, ". Messabfrage")
    time.sleep(schleifenPause)
    schleifenZaehler = schleifenZaehler + 1

print("Temperaturabfrage beendet")