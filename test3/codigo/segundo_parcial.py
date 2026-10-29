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
#Clase parent
botones = 5
check = 0
dato_random = 0
# class Main_window(QDialog):

class MainWindow(QMainWindow):

    def __init__(self):
        super(MainWindow, self).__init__()
        self.title = "Proyecto final"
        self.setWindowTitle(self.title)
        self.lista_paciente = []

        #Definir icono
        my_icon = QIcon()
        my_icon.addFile('Images/Logo_del_ITESM.svg')
        self.setWindowIcon(my_icon)

        self.UI()
        # label = QLabel(self)
        # pixmap = QPixmap(img)
        # label.setPixmap(pixmap)
        # self.setCentralWidget(label)
        # self.resize(0.75*pixmap.width(), 0.75*pixmap.height())

    def UI(self):
        #Agregar Witdget
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.setGeometry(0, 0, w, h)

        #Crear etiquetas para el menu
        self.nombre_l = QLabel("Nombre");
        self.nombre_l.setFont(QFont("Arial", 15))

        self.boton = []
        menu = QHBoxLayout(self.main_widget)

        for i in range(botones):
            temp = QPushButton('', self)
            temp.setFixedSize(w/(botones+1), h/(botones+1))
            self.boton.append(temp)
            menu.addWidget(self.boton[i])
        self.setLayout(menu)

        self.boton[0].pressed.connect(self.boton_0)
        self.boton[1].pressed.connect(self.boton_1)
        self.boton[2].pressed.connect(self.boton_2)
        self.boton[3].pressed.connect(self.boton_3)
        self.boton[4].pressed.connect(self.boton_4)

    def boton_0(self):
        check = 0
        if(self.check_data(check)):
            print("Si!")
    def boton_1(self):
        check = 1
    def boton_2(self):
        check = 2
    def boton_3(self):
        check = 3
    def boton_4(self):
        check = 4

    def check_data(self,check):
        if(check == dato_random):
            return True
        else:
            return False

stylesheet = """
    MainWindow {
        background-image: url('Images/luces.jpg');
        background-repeat: no-repeat; 
        background-position: center;
    }
"""

#"D:wallpaper.jpg");
if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)  # <---
    window = MainWindow()
    window.resize(w, h)
    window.show()
    sys.exit(app.exec())