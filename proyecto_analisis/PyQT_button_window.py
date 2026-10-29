import sys
from PySide6.QtWidgets import (QLineEdit, QPushButton, QApplication,
    QVBoxLayout, QDialog, QWidget)

class Form(QWidget):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        self.edit = QLineEdit("Write my name here")
        self.button_pop = QPushButton("POP!")
        self.button_push = QPushButton("PUSH!")
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.edit)
        layout.addWidget(self.button_pop)
        layout.addWidget(self.button_push)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.button_pop.clicked.connect(self.pop_data)
        self.button_push.clicked.connect(self.push_data)
    # Greets the user
    def pop_data(self):
        print(f"POP! {self.edit.text()}")

    def push_data(self):
        print(f"PUSH! {self.edit.text()}")

if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())