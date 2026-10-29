#############################################################################
#############################################################################


#Bibliotecas necesarias para nuestro proyecto
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys, os
from PIL import Image

#Definir la imagen, para tener tanto el ancho como el largo
im = Image.open("Images/luces.jpg")
w, h = im.size
print('width: ', w)
print('height:', h)
iconroot = os.path.dirname(__file__)


#Palabra metida a nuestro sistema para adivinar
Palabra = "No"
len_palabra = len(Palabra)
Palabra_ahorcado = list("_"*len_palabra)
temp = ["" for x in range(len_palabra)]
Palabra_check = ["" for x in range(len_palabra)]

class WidgetGallery(QWidget):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)
        self.vidas = 3
        self.setWindowTitle("Ahorcado Game")
        self.changeStyle('Windows')
        
        #Imagen
        self.buckling_clabel = QLabel(self)
        pixmap = QPixmap(os.path.join(iconroot, "Images/icon.png"))
        self.buckling_clabel.resize(50, 50)
        self.buckling_clabel.setPixmap(pixmap.scaled(self.buckling_clabel.size(), Qt.KeepAspectRatio))
        
        
        
        #Palabra
        self.Data = QLabel("".join(Palabra_ahorcado))
        self.Data.setFont(QFont('Times', 50))
        self.Data.setAlignment(Qt.AlignCenter)

        # Vidas
        self.data_vidas = QLabel(str(self.vidas))
        self.data_vidas.setFont(QFont('Times', 50))
        self.data_vidas.setAlignment(Qt.AlignCenter)

        #Boton
        self.pushButton2 = QPushButton("Check!")
        self.pushButton2.setFont(QFont('Times', 20))
        self.pushButton2.setStyleSheet("background-color: none; color: red;")
        self.pushButton2.clicked.connect(self.revisar_palabra)
        
        #Cuadros para editar
        text_group = QHBoxLayout()
        for i in range(len_palabra):
            temp[i] = QLineEdit()
            temp[i].setFixedSize(50,50)
            text_group.addWidget(temp[i])
    
        mainLayout = QGridLayout()
        mainLayout.addWidget(self.buckling_clabel,1,0)
        mainLayout.addWidget(self.Data,0,1,2,10)
        mainLayout.addLayout(text_group,6,1,1,10)
        mainLayout.addWidget(self.pushButton2,15,4,2,4)
        mainLayout.addWidget(self.data_vidas,20,1,2,10)
        self.setLayout(mainLayout)
    
    
    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        self.changePalette()
        
    def changePalette(self):
            QApplication.setPalette(QApplication.style().standardPalette())

    def revisar_palabra(self):
        
        for i in range(len_palabra):
            self.valido = True
            # print(str(temp[i].text()))
            if(Palabra[i] == temp[i].text()):
                Palabra_ahorcado[i] = Palabra[i]
            elif(str(temp[i].text()) == ""):
                Palabra_ahorcado[i] = Palabra_ahorcado[i]
            else:
                self.valido = False
#                 Palabra_ahorcado[i] = str(temp[i].text())
        if(self.valido == False):
            self.vidas = self.vidas - 1;
            self.data_vidas.setText(str(self.vidas))

        str_palabra = "".join(Palabra_ahorcado)
        self.Data.setText(str_palabra)
        if(str_palabra == Palabra):
            self.Data.setStyleSheet('color: green')
        if(self.vidas == 0):
            self.Data.setStyleSheet('color: red')
            self.pushButton2.setDisabled(True)
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
