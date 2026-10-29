import sys,os
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from pathlib import Path


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # snip

        self.pick_btn = QPushButton("Pick")
        self.pick_btn.setObjectName("Pick")
        self.pick_btn.clicked.connect(self.start_selection)

    def start_selection(self):
        # Repeating timer, calls random_pick over and over.
        self.picktimer = QTimer()
        self.picktimer.setInterval(500)
        self.picktimer.timeout.connect(self.random_pick)
        self.picktimer.start()

        # Single oneshot which stops the selection after 5 seconds
        QTimer.singleShot(5000, self.stop_selection)

    def stop_selection(self):
        # Stop the random selection
        self.picktimer.stop()

        # The current pick is in self.current_selection
        print("Current selection is: ", self.current_selection)


    def random_pick(self):

        buckling_blabel = QLabel(self)
        pixmap = QPixmap(os.path.join(iconroot, "Images/logo_tec.png"))
        buckling_blabel.resize(0.25 * pixmap.width(), 0.25 * pixmap.height())
        buckling_blabel.setPixmap(pixmap.scaled(buckling_blabel.size(), Qt.KeepAspectRatio))
        buckling_blabel.setAlignment(Qt.AlignCenter)

        # Store the current selection, so we have it at the end in stop_selection.
        self.current_selection = "12"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setStyleSheet(stylesheet)  # <---
    window = MainWindow()
    window.show()
    sys.exit(app.exec())