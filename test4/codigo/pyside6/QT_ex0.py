import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import QSize
from numpy.random import choice
from PySide6.QtGui import *

window_titles = [
    "My App",
    "My App",
    "Still My App",
    "Still My App",
    "What on earth",
    "What on earth",
    "This is surprising",
    "This is surprising",
    "Something went wrong",
]

# class Color(QWidget):
#
#     def __init__(self, color):
#         super(Color, self).__init__()
#         self.setAutoFillBackground(True)
#         palette = self.palette()
#         palette.setColor(QPalette.ColorRole.Window, QColor(color))
#         self.setPalette(palette)
#
# class MainWindow(QMainWindow):
#
#     def __init__(self):
#         super(MainWindow, self).__init__()
#
#         self.setWindowTitle("My App")
#
#         layout = QGridLayout()
#
#         layout.addWidget(Color('red'), 0, 0)
#         layout.addWidget(Color('green'), 1, 1)
#         layout.addWidget(Color('blue'), 2, 2)
#         layout.addWidget(Color('purple'), 3, 0, 1, 3)
#
#         widget = QWidget()
#         widget.setLayout(layout)
#         self.setCentralWidget(widget)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_times_clicked = 0

        self.setWindowTitle("My App")
        self.setFixedSize(QSize(800, 600))

        self.button = QPushButton("Press Me!")
        self.button.clicked.connect(self.the_button_was_clicked)

        self.windowTitleChanged.connect(self.the_window_title_changed)

        self.setCentralWidget(self.button)

    def the_button_was_clicked(self):
        print("Clicked.")
        new_window_title = choice(window_titles)
        print("Setting title:  %s" % new_window_title)
        self.setWindowTitle(new_window_title)

    def the_window_title_changed(self, window_title):
        print("Window title changed: %s" % window_title)

        if window_title == "Something went wrong":
            self.button.setDisabled(True)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()