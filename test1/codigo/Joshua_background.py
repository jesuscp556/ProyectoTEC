from PySide6.QtWidgets import *
from PySide6.QtCore import *
import sys

from PIL import Image

im = Image.open('../Images/luces.jpg')


w, h = im.size
print('width: ', w)
print('height:', h)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        # self.pushButton1 = QPushButton("Button 1", self.centralwidget)
        self.pushButton2 = QPushButton("Check!", self.centralwidget)
        self.pushButton2.setFixedHeight(40)

        self.Data = QLabel("A ver!")

        lay = QVBoxLayout(self.centralwidget)

        lay.addWidget(self.Data)
        lay.addWidget(self.pushButton2)

#         background-image: url("/Users/joshuamenchaca/Desktop/PrepaTec/interior.jpeg");

stylesheet = """
    MainWindow {
        background-image: url('../Images/luces.jpg'); 
        background-repeat: no-repeat; 
        background-position: center;
    }
"""

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setStyleSheet(stylesheet)     # <---
    window = MainWindow()
    window.resize(w, h)
    window.show()
    sys.exit(app.exec())