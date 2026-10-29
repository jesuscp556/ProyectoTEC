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

class UI(QWidget):
    def __init__(self, parent=None):
        super(UI, self).__init__(parent)
        # Agregar Witdget
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.setGeometry(0, 0, w, h)

        # Crear etiquetas para el menu
        self.nombre_l = QLabel("Nombre");
        self.nombre_l.setFont(QFont("Arial", 15))

        self.sexo_l = QLabel("Sexo");
        self.sexo_l.setFont(QFont("Arial", 15))
        self.sexo_l.setStyleSheet("color: white;")

        self.edad_l = QLabel("Edad");
        self.edad_l.setFont(QFont("Arial", 15))
        self.edad_l.setStyleSheet("color: white;")

        # EDITOR
        self.nombre = QLineEdit()
        self.nombre.setAlignment(Qt.AlignCenter)
        self.nombre.setFixedWidth(200)
        # self.nombre.setFixedSize(100, 50)
        self.nombre.setEchoMode(QLineEdit.EchoMode.Password)

        # Imagen
        buckling_blabel = QLabel(self)
        pixmap = QPixmap(os.path.join(iconroot, "Images/logo_tec.png"))
        buckling_blabel.resize(0.25 * pixmap.width(), 0.25 * pixmap.height())
        buckling_blabel.setPixmap(pixmap.scaled(buckling_blabel.size(), Qt.KeepAspectRatio))
        buckling_blabel.setAlignment(Qt.AlignCenter)

        # COMBO BOX
        self.sexo = QComboBox()
        edad = []
        for i in range(21):
            edad.append(str(i))
        self.sexo.addItems(edad)

        self.button_push = QPushButton("Reset")
        self.button_push.setFont(QFont("Helvetica [Cronyx]", 15))
        # self.button_push.adjustSize()

        self.etiqueta = QLabel("Probando 1-2-3")
        self.etiqueta.setFont(QFont("Arial", 30))

        # Create layout and add widgets

        menu_layout = QVBoxLayout()
        menu_layout.addWidget(self.nombre_l)
        menu_layout.addWidget(self.nombre)
        menu_layout.addWidget(self.sexo_l)
        menu_layout.addWidget(self.sexo)
        menu_layout.addWidget(self.button_push)
        menu_layout.setAlignment(Qt.AlignCenter)

        # Set dialog layout
        # menu = QGridLayout(self.main_widget)
        # menu.addWidget(buckling_blabel,0,0)
        # menu.addLayout(menu_layout,0,1)
        # menu.setAlignment(Qt.AlignCenter)
        menu = QHBoxLayout(self.main_widget)
        menu.addWidget(buckling_blabel)
        menu.addLayout(menu_layout)
        menu.setAlignment(Qt.AlignCenter)

        self.setLayout(menu)


