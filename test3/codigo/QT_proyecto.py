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

        #Imagen
        buckling_blabel = QLabel(self)
        pixmap = QPixmap(os.path.join(iconroot, "Images/logo_tec.png"))
        buckling_blabel.resize(0.25*pixmap.width(), 0.25*pixmap.height())
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
        #self.button_push.adjustSize()

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

        # Add button signal to greetings slot

        self.button_push.pressed.connect(self.push_data)
        self.button_push.released.connect(self.soltar)

    # Greets the user


    def push_data(self):
        self.lista_paciente.append([self.nombre.text(),str(self.sexo.currentText())])
        self.button_push.setStyleSheet("background-color: green; color: white;")
        self.dialogo = QMessageBox.information(
                self, "Revision", "Los datos son los siguientes: \n" + str(self.lista_paciente[-1]))


    def soltar(self):
        print("YA JALO! - soltado")
        self.button_push.setStyleSheet("background-color: none; color: black;")

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