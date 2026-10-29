import sys
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *


# class Main_window(QDialog):
class Main_window(QWidget):
    def __init__(self, parent=None):
        super(Main_window, self).__init__(parent)
        # Create widgets
        self.setGeometry(100, 100, 600, 400)

        self.setAutoFillBackground(True)

        self.button_pop = QPushButton("Nooooo!")
        self.button_pop.setFont(QFont('Arial', 15))
        # self.button_pop.setFixedSize(100,50)
        self.button_pop.setFixedHeight(40)
        self.button_pop.setFixedWidth(200)
        self.button_pop.setStyleSheet("background-color: red; color: black;")

        #EDITOR
        self.nombre = QLineEdit()
        self.nombre.setFixedSize(100,50)
        self.nombre.setEchoMode(QLineEdit.EchoMode.Password)

        #COMBO BOX
        self.sexo = QComboBox()
        self.sexo.addItems(["Masculino","Femenino"])


        self.button_push = QPushButton("Reset")
        self.button_push.setFont(QFont("Helvetica [Cronyx]", 15))
        self.button_push.adjustSize()

        self.etiqueta = QLabel("Probando 1-2-3")
        self.etiqueta.setFont(QFont("Arial", 30))

        # Create layout and add widgets
        
        layout = QGridLayout()
        # layout = QVBoxLayout()
        # layout = QHBoxLayout()
        layout.addWidget(self.button_pop)
        layout.addWidget(self.nombre)
        layout.addWidget(self.button_push)
        # Set dialog layout
        
        self.setLayout(layout)
        
        # Add button signal to greetings slot
        
        self.button_pop.clicked.connect(self.pop_data)
        self.button_push.pressed.connect(self.push_data)
        self.button_push.released.connect(self.soltar)
    # Greets the user

    def pop_data(self):
        print("NO JALA")
        self.button_pop.setDisabled(True)
        self.button_push.setStyleSheet("background-color: black; color: white;")
        self.button_pop.setStyleSheet("background-color: red; color: white;")


        self.dato = self.nombre.text()
        print(self.dato)


    def push_data(self):
        print("YA JALO! - presionado")
        self.button_push.setStyleSheet("background-color: green; color: white;")
        self.button_pop.setStyleSheet("background-color: none; color: black;")
        self.button_pop.setEnabled(True)
    def soltar(self):
        print("YA JALO! - soltado")
        self.button_push.setStyleSheet("background-color: none; color: black;")


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    GUI = Main_window()
    GUI.show()
    # Run the main Qt loop
    sys.exit(app.exec())