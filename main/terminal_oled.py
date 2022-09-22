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

# Define the Reset Pin
oled_reset = digitalio.DigitalInOut(board.D4)

# Display Parameters
WIDTH = 128
HEIGHT = 64
BORDER = 5

# Display Refresh
LOOPTIME = 1.0

# Use for I2C.
i2c = board.I2C()
oled = adafruit_ssd1306.SSD1306_I2C(WIDTH, HEIGHT, i2c, addr=0x3C, reset=oled_reset)

# Clear display.
oled.fill(0)
oled.show()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
image = Image.new("1", (oled.width, oled.height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a white background
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
        messdaten_humidity = aktuelleHumidity()
        messdaten_temperatur = aktuelleTemperatur()
        messdaten_level = aktuellerWasserstand()
        printText(messdaten_level, messdaten_temperatur, messdaten_humidity)
        draw.text((0, 0), "Skyfarm to the moon", font=font, fill=255)
        draw.text((0, 16), "Temperatur :" + str(messdaten_temperatur), font=font, fill=255)
        # draw.text((80, 16), str(Temp, 'utf-8'), font=font, fill=255)
        draw.text((0, 32), "Feuchtigkeit :" + str(messdaten_humidity) + " %", font=font, fill=255)
        draw.text((0, 48), "Wasserstand :" + str(messdaten_level), font=font, fill=255)

        # Display image
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