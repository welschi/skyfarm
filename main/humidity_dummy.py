#######################################################################################################################
##  Importiere alle Bibs, im Dummy keine vorhanden

#######################################################################################################################
##  DHT22 Sensor mit GPIO Pin 26 gezeichnet, nicht drin in dummy

# dhtDevice = adafruit_dht.DHT22(board.D26, use_pulseio=False)

#######################################################################################################################
##  Funktion zum Auslesen

def aktuelleHumidityDummy():
    humidity_dummy = 24.578
    return humidity_dummy