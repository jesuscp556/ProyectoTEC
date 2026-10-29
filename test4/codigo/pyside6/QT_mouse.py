from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import QApplication, QWidget, QHBoxLayout, QLabel

import sys


class Main(QWidget):

    def __init__(self, parent=None):
        super(Main, self).__init__(parent)

        layout  = QHBoxLayout(self)
        layout.addWidget(QLabel("this is the main frame"))

    def mousePressEvent(self, QMouseEvent):
        #print mouse position
        print(QMouseEvent.pos())

a = QApplication([])
m = Main()
m.show()
sys.exit(a.exec_())