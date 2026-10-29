import sys,os
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from numpy import *
import random as rd

"""Battleship"""
len_button = 150

class Main_window(QWidget):
    def __init__(self, parent=None):
        super(Main_window, self).__init__(parent)
        # Create widgets
        self.setGeometry(0,0,800,600)
        self.title = "BattleShip"
        self.setWindowTitle(self.title)
        # self.setGeometry(300, 50, 320, 420)

        my_icon = QIcon()
        my_icon.addFile('Images/Icons/crucero.png')
        self.setWindowIcon(my_icon)


        self.boton1 = QPushButton()
        self.boton2 = QPushButton()
        self.boton3 = QPushButton()
        self.boton4 = QPushButton()
        self.boton5 = QPushButton()
        self.boton6 = QPushButton()
        self.boton7 = QPushButton()
        self.boton8 = QPushButton()
        self.boton9 = QPushButton()

        self.boton1.setFixedSize(len_button, len_button)
        self.boton2.setFixedSize(len_button, len_button)
        self.boton3.setFixedSize(len_button, len_button)
        self.boton4.setFixedSize(len_button, len_button)
        self.boton5.setFixedSize(len_button, len_button)
        self.boton6.setFixedSize(len_button, len_button)
        self.boton7.setFixedSize(len_button, len_button)
        self.boton8.setFixedSize(len_button, len_button)
        self.boton9.setFixedSize(len_button, len_button)

        self.boton_reset = QPushButton("Reset")
        self.boton_reset.setFont(QFont('times', 12))

        #Etiqueta
        self.Etiqueta = QLabel("Posicion del barco")
        self.Etiqueta.setAlignment(Qt.AlignCenter)

        # EDITOR
        self.texto = QLineEdit()
        self.texto.setAlignment(Qt.AlignCenter)
        # self.nombre.setFixedSize(100, 50)
        self.texto.setEchoMode(QLineEdit.EchoMode.Password)

        mar = QGridLayout()
        mar.addWidget(self.boton1, 0, 0)
        mar.addWidget(self.boton2, 0, 1)
        mar.addWidget(self.boton3, 0, 2)
        mar.addWidget(self.boton4, 1, 0)
        mar.addWidget(self.boton5, 1, 1)
        mar.addWidget(self.boton6, 1, 2)
        mar.addWidget(self.boton7, 2, 0)
        mar.addWidget(self.boton8, 2, 1)
        mar.addWidget(self.boton9, 2, 2)


        menu = QGridLayout()
        menu.addWidget(self.Etiqueta,0,0)
        menu.addWidget(self.texto,0,1)
        menu.addWidget(self.boton_reset,1,0,1,2)

        juego = QHBoxLayout(self)
        juego.addLayout(mar)
        juego.addLayout(menu)

        #Funciones
        # self.boton1.clicked.connect(self.check_posicion1)
        # self.boton2.clicked.connect(self.check_posicion2)
        # self.boton3.clicked.connect(self.check_posicion3)
        # self.boton4.clicked.connect(self.check_posicion4)
        # self.boton5.clicked.connect(self.check_posicion5)
        # self.boton6.clicked.connect(self.check_posicion6)
        # self.boton7.clicked.connect(self.check_posicion7)
        # self.boton8.clicked.connect(self.check_posicion8)
        # self.boton9.clicked.connect(self.check_posicion9)

        self.boton_reset.clicked.connect(self.reset_game)

    def reset_game(self):
        self.barco = int(int(self.texto.text()))
        print(self.barco)



if __name__ == "__main__":
    # crea la aplicacion
    app = QApplication(sys.argv)
    # crea y muestra la ventana
    gato = Main_window()
    gato.show()
    # corre la app
    sys.exit(app.exec())