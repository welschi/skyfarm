from temperatur import aktuelleTemperatur
from humidity import aktuelleHumidity, dhtDevice
from level import aktuellerWasserstand

import datetime
import time
import board
import busio
import digitalio
import os

from PIL import Image, ImageDraw, ImageFont
import adafruit_ssd1306

import subprocess

zaehler = 0
anzahl = 1000000
pause = 0.0001

# Definiere den Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)

# Display Parameter
WIDTH = 128
HEIGHT = 64
BORDER = 5

# Display Refresh
LOOPTIME = 1.0

# I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

# Lösche Display.
oled.fill(0)
oled.show()

# Erzeuge ein leeres Bild zum Zeichnen.
# Gehe sicher ein Bild im Mode '1' für 1-bit Farbe zu erzeugen.
image = Image.new("1", (oled.width, oled.height))

# Lass das Zeichen Objekt ein Bild zeichnen.
draw = ImageDraw.Draw(image)

# Erzeuge einen weißen Hintergrund
draw.rectangle((0, 0, oled.width, oled.height), outline=255, fill=255)

font = ImageFont.truetype('PixelOperator.ttf', 16)


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

        # Erzeuge ein schwarz gefülltes Rechteck als Hintergrund.
        draw.rectangle((0, 0, oled.width, oled.height), outline=0, fill=0)

        messdaten_humidity = aktuelleHumidity()
        messdaten_temperatur = aktuelleTemperatur()
        messdaten_level = aktuellerWasserstand()
        printText(messdaten_level, messdaten_temperatur, messdaten_humidity)
        currentTime = datetime.datetime.now()
        i = currentTime.strftime("%H:%M:%S")

        draw.text((0, 0), "Skyfarm: " + i, font=font, fill=255)
        draw.text((0, 16), "Temperatur: " + str(messdaten_temperatur), font=font, fill=255)
        draw.text((0, 32), "Feuchtigkeit: " + str(messdaten_humidity) + " %", font=font, fill=255)
        draw.text((0, 48), "Wasserstand: " + str(messdaten_level), font=font, fill=255)

        # Zeige Bild
        oled.image(image)
        oled.show()
        time.sleep(LOOPTIME)

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