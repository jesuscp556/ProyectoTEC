import sys,os
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *

#IMG
iconroot = os.path.dirname(__file__)
from PIL import Image
# im = Image.open('D:wallpaper.jpg')
im = Image.open('Images/luces.jpg')
w, h = im.size
print('width: ', w)
print('height:', h)

filas = 3
columnas = 3
len_button = 150


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        title = "TIC TAC TOE"
        self.setWindowTitle(title)
        self.resize(w, h)

        self.Player = False

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.setGeometry(0, 0, w, h)

        self.boton = []
        menu = QGridLayout(self.main_widget)

        for i in range(columnas*filas):
            temp = QPushButton('',self)
            temp.setFixedSize(len_button,len_button)
            self.boton.append(temp)
            menu.addWidget(self.boton[i],i/columnas,i%filas)
        self.setLayout(menu)

        self.boton[0].pressed.connect(self.boton_0)
        self.boton[1].pressed.connect(self.boton_1)
        # self.boton[2].pressed.connect(self.boton_2)
        # self.boton[3].pressed.connect(self.boton_3)
        # self.boton[4].pressed.connect(self.boton_4)
        # self.boton[5].pressed.connect(self.boton_5)
        # self.boton[6].pressed.connect(self.boton_6)
        # self.boton[7].pressed.connect(self.boton_7)
        # self.boton[8].pressed.connect(self.boton_8)

    def boton_0(self):
        if(self.Player):
            self.boton[0].setStyleSheet("background-color: transparent ; color: Green;")
            # self.boton[0].setIcon(QIcon('Images/tache.png'))
            # self.boton[0].setIconSize(QSize(len_button, len_button))
            self.boton[0].setText("X")
            self.boton[0].setFont(QFont("Arial", len_button-5))

        else:
            # self.boton[0].setStyleSheet("background-color: transparent ; color: white;")
            # self.boton[0].setIcon(QIcon('Images/circulo.png'))
            self.boton[0].setStyleSheet("color: Red;")
            # self.boton[0].setIcon(QIcon('Images/tache.png'))
            # self.boton[0].setIconSize(QSize(len_button, len_button))
            self.boton[0].setText("O")
            self.boton[0].setFont(QFont("Arial", len_button-5))

        self.boton[0].setDisabled(True)
        self.Player = not self.Player

    def boton_1(self):
        self.boton[1].setDisabled(True)
        if(self.Player):
            self.boton[1].setStyleSheet("background-color: Green; color: white;")
        else:
            self.boton[1].setStyleSheet("background-color: Red; color: white;")
        self.Player = not self.Player



stylesheet = """
    MainWindow {
        background-image: url('Images/luces.jpg');
        background-repeat: no-repeat; 
        background-position: center;
    }
"""



if __name__ == "__main__":
    app = QApplication(sys.argv)

    app.setStyleSheet(stylesheet)  # <---
    window = MainWindow()
    #     window.setStyleSheet("background-color: white")
    window.resize(w, h)
    window.show()
    sys.exit(app.exec())