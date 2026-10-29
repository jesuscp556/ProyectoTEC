import sys
from pathlib import Path

from PySide6 import QtCore, QtMultimedia, QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)

        mainLayout = QtWidgets.QVBoxLayout(self)
        self.playButton = QtWidgets.QPushButton(text="Play")
        self.pauseButton = QtWidgets.QPushButton(text="Pause")
        mainLayout.addWidget(self.playButton)
        mainLayout.addWidget(self.pauseButton)

        self.soundEffect = QtMultimedia.QSoundEffect()
        self.soundEffect.setSource("file:./Images/tech_sound.wav")
        self.soundEffect.setLoopCount(3)

        self.playButton.clicked.connect(self.soundEffect.play)
        self.pauseButton.clicked.connect(self.soundEffect.stop)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    widget = MyWidget()
    widget.resize(200, 100)
    widget.show()
    sys.exit(app.exec())