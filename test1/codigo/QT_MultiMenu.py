from pathlib import Path

#INGRESO DE BIBLIOTECA DE PROYECTO
from QT_capturista import *


#IMG
iconroot = os.path.dirname(__file__)
from PIL import Image
# im = Image.open('D:wallpaper.jpg')
# im = Image.open('Images/lake_resize.jpg')
im = Image.open('Images/luces.jpg')
w, h = im.size
print(str(w) + "\n" + str(h))


def absPath(file):
    return str(Path(__file__).parent.absolute() / file)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        title = "Hospital General de Occidente"
        self.setWindowTitle(title)
        self.resize(w, h)

        # Definir icono
        my_icon = QIcon()
        my_icon.addFile('Images/Logo_del_ITESM.svg')
        self.setWindowIcon(my_icon)

        #Definir CentralWidget
        self.main_widget = QWidget(self)
        # self.setGeometry(0, 0, 800, 600)
        # self.centralWidget = QWidget(self)
        # self.setCentralWidget(self.centralWidget)
        # self.setGeometry(0, 0, w, h)

        # construimos nuestro menú
        self.construir_menu()

    def construir_menu(self):
        # Recuperamos la barra de menú
        self.menu = self.menuBar()

        # Añadimos un menú de archivo
        # self.menu_rapido = self.menu.addMenu("&Ejemplo")
        self.menu_archivo = self.menu.addMenu("&Modo")

        # Añadimos una acción de prueb

        self.menu_archivo.addAction(QIcon(absPath("Images\Icons\stethoscope.png")),"&Medico", self.medico_widget,"Ctrl+M")

        self.menu_archivo.addAction(QIcon(absPath("Images\Icons\medical-checkup.png")),"&Capturista",self.capturista,"Ctrl+T")

        self.menu_archivo.addAction(QIcon(absPath("Images\Icons\\user.png")),"&Paciente","Ctrl+P")

        self.menu_archivo.addAction(QIcon(absPath("Images\Icons\info.png")),"&Información",self.imagen,"Ctrl+I")

        self.menu_archivo.addAction(QIcon(absPath("Images\Icons\logout.png")), "&Salir", self.close, "Ctrl+Q")
        # Añadimos un submenú

    def medico_widget(self):

        self.Botonazo = QPushButton("No!")
        self.setCentralWidget(self.Botonazo)

    def imagen(self):
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)
        self.imagen_menu = QLabel(self)
        pixmap = QPixmap(os.path.join(iconroot, "Images/Emergency.webp"))
        self.imagen_menu.resize(0.5 * pixmap.width(), 0.5 * pixmap.height())
        self.imagen_menu.setPixmap(pixmap.scaled(self.imagen_menu.size(), Qt.KeepAspectRatio))
        self.imagen_menu.setAlignment(Qt.AlignCenter)
        self.setCentralWidget(self.imagen_menu)

    def dialogo(self):
        self.dialogo = QMessageBox.information(self, "Diálogo informativo", "Esto es un texto informativo")

    def capturista(self):
        # Agregar Witdget
        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)


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
    window.resize(w,h)
    window.show()
    sys.exit(app.exec())