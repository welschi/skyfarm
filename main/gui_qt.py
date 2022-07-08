## Main Gui file zum Ausführen

########################################################################################################################
##  import alle packages

from PySide6.QtWidgets import QApplication, QMainWindow
from gui_main import Ui_gui_main
from temperatur_dummy import aktuelleTemperatur



########################################################################################################################
##  Oberklasse definiert Frm_Main über QMainWindow

class Frm_Main(QMainWindow, Ui_gui_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

def test_change():
    temperatur_string = "Temperatur: " + str(aktuelleTemperatur())
    temp_label = gui_main.lb_temp
    temp_label.setText(temperatur_string)

########################################################################################################################
##  Ausführen der App

test_app = QApplication()
gui_main = Frm_Main()

gui_main.bt_refresh.clicked.connect(test_change)

gui_main.show()
test_app.exec()
