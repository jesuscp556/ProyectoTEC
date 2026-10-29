import sys
from PySide6.QtGui import QMovie
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication()
label = QLabel("hello")
movie = QMovie("Images/tech_issues.gif")
print(movie.isValid())
label.setMovie(movie)
movie.start()
label.show()
sys.exit(app.exec())