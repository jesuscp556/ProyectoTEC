import sys,os
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class Caja(QLabel):
    def __init__(self, color):
        super().__init__()
        self.setStyleSheet(f"background-color:{color}")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(800,600)

        my_icon = QIcon()
        my_icon.addFile('Images/Logo_del_ITESM.svg')
        self.setWindowIcon(my_icon)

        # creamos un layout de pestañas
        tabs = QTabWidget()



        boton = QPushButton("Data");
        boton.setFixedSize(100,50)

        # Añadimos varios widgets como pestañas con nombres
        tabs.addTab(boton,"Boton")
        tabs.addTab(Caja("magenta"), "Dos")
        tabs.addTab(Caja("purple"), "Tres")
        tabs.addTab(Caja("red"), "Cuatro")

        # asignamos las pestañas como widget central
        self.setCentralWidget(tabs)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())