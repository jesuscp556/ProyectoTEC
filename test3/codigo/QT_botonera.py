#############################################################################
#############################################################################


#Bibliotecas necesarias para nuestro proyecto
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import sys, os
from PIL import Image

from numpy import random


#Definir la imagen, para tener tanto el ancho como el largo
im = Image.open("Images/luces.jpg")
w, h = im.size
print('width: ', w)
print('height:', h)
# iconroot = os.path.dirname(__file__)


class WidgetGallery(QWidget):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)
        self.setWindowTitle("Buscaminas")
        self.changeStyle('fusion')
        self.cuadricula = 5
        self.numero = random.randint(0,self.cuadricula*self.cuadricula - 1)
        print(self.numero)
        self.Box = ["" for x in range(self.cuadricula)]
        self.Botones = ["" for x in range(self.cuadricula*self.cuadricula)]
        self.indice = 0
        
        self.layout = QGridLayout()
        for i in range(self.cuadricula):
            for j in range(self.cuadricula):
                self.indice = (self.cuadricula*i) + j
                self.Botones[self.indice] = QPushButton(str(self.indice + 1))
                self.Botones[self.indice].setFixedSize(100,100)
                
                nombre = "Button" + str(self.indice)
                self.Botones[self.indice].setAccessibleName(nombre)
                
                self.layout.addWidget(self.Botones[self.indice],i,j)
                self.Botones[self.indice].clicked.connect(self.checar_boton)
#                 print(str(self.indice))
                
        self.setLayout(self.layout)
        
        
    def changeStyle(self, styleName):
        QApplication.setStyle(QStyleFactory.create(styleName))
        QApplication.setPalette(QApplication.style().standardPalette())
    
    def checar_boton(self):
        print("Checando " +str(self.Botones[self.indice].accessibleName()))
        
if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    
    GUI = WidgetGallery()
    GUI.resize(w, h)
    GUI.show()
    sys.exit(app.exec())