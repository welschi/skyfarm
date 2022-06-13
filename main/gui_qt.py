########################################################################################################################
#  import alle packages

from PySide6.QtWidgets import QApplication, QMainWindow

########################################################################################################################
#  Oberklasse definiert Frm_Main über QMainWindow

class Frm_Main(QMainWindow):
    def __init__(self):
        super().__init__()

########################################################################################################################
#  Ausführen der App

test_app = QApplication()
gui_main = Frm_Main()

gui_main.show()
test_app.exec()