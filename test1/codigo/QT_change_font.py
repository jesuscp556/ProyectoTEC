from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6.QtCore import *
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(700, 300)
        self.setWindowTitle("CodersLegacy")
        self.setContentsMargins(20, 20, 20, 20)

        id = QFontDatabase.addApplicationFont("Frostbite.ttf")
        if id < 0: print("Error")

        families = QFontDatabase.applicationFontFamilies(id)
        print(families)

        self.label = QLabel("Hello World", self)
        self.label.setFont(QFont(families[0], 90))
        # self.label.setAlignment(Qt.AlignCenter)
        self.label.move(50, 100)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())