## Main Gui file zum Ausführen

## Befehle:
## pyside6-designer --> Öffnen des QT Designers
## pyside6-uic gui_main.ui -o gui_main.py --> Umwandeln der .ui Datei in .py Datei

########################################################################################################################
##  import alle packages

from PySide6.QtWidgets import QApplication, QMainWindow
from gui_main import Ui_gui_main
from temperatur_dummy import aktuelleTemperaturDummy
from humidity_dummy import aktuelleHumidityDummy


########################################################################################################################
##  Oberklasse definiert Frm_Main über QMainWindow

class Frm_Main(QMainWindow, Ui_gui_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

def Temperatur():
    temperatur_string = "Temperatur: " + str(aktuelleTemperaturDummy())
    temp_label = gui_main.lb_temp
    temp_label.setText(temperatur_string)

def Luftfeuchtigkeit():
    humidity_string = "Luftfeuchtigkeit: " + str(aktuelleHumidityDummy())
    humidity_label = gui_main.lb_humidity
    humidity_label.setText(humidity_string)


########################################################################################################################
##  Ausführen der App

test_app = QApplication()
gui_main = Frm_Main()

gui_main.bt_refresh.clicked.connect(Temperatur)
gui_main.bt_refresh.clicked.connect(Luftfeuchtigkeit)

gui_main.show()
test_app.exec()
