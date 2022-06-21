## Main Gui file zum Ausführen

########################################################################################################################
##  import alle packages

from PySide6.QtWidgets import QApplication, QMainWindow
from gui_main import Ui_gui_main


########################################################################################################################
##  Oberklasse definiert Frm_Main über QMainWindow

class Frm_Main(QMainWindow, Ui_gui_main):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


########################################################################################################################
##  Ausführen der App

test_app = QApplication()
gui_main = Frm_Main()

gui_main.show()
test_app.exec()
