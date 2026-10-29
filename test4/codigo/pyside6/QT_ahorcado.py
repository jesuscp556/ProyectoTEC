#############################################################################
#############################################################################


#Bibliotecas necesarias para nuestro proyecto
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys
from PIL import Image

#Definir la imagen, para tener tanto el ancho como el largo
im = Image.open('Images/luces.jpg')
w, h = im.size
print('width: ', w)
print('height:', h)

#Palabra metida a nuestro sistema para adivinar
Palabra = "Aprobado"


class WidgetGallery(QMainWindow):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)
        
        self.setWindowTitle("AHORCADO GAME")
        self.originalPalette = QApplication.palette("Fusion")
        
        self.Data = QLabel(Palabra)
        self.Data.setFont(QFont('Times', 40))
        self.Data.setAlignment(Qt.AlignCenter)

        self.pushButton2 = QPushButton("Check!")
        self.pushButton2.setFont(QFont('Times', 25))
        self.pushButton2.setStyleSheet("background-color: none; color: red;")
        self.pushButton2.clicked.connect(self.revisar_palabra)
        
        
        # Create layout and add widgets
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        
        # Create Horizontal Layout
        List_q = QHBoxLayout(self.centralwidget)
        for i in range(8):
            temp = QTextEdit()
            temp.setFixedSize(50,50)
            List_q.addWidget(temp)
        
        # Set dialog layout
        layout = QVBoxLayout(self.centralwidget)
        self.setLayout(layout)
        layout.addWidget(self.Data)
        layout.addWidget(self.pushButton2, alignment=Qt.AlignCenter)

        accion_info = QAction("", self)
        accion_info.setShortcut("Ctrl+Q")
    def revisar_palabra(self):
        self.Data.setText("Cambio!")

stylesheet = """
    WidgetGallery {
        background-image: url("Images/luces.jpg"); 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)     # <---
    
    gallery = WidgetGallery()
    gallery.resize(w, h)
    gallery.show()
    sys.exit(app.exec())