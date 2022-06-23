
# Create a message text box, button, GUI
import sys
# imports widgets: namely QLabel, QPushButton, and QMessageBox.
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox

# defines method dialog: creates message box widget (sets text buttons and other fields)
def dialog():
    mbox = QMessageBox()

    mbox.setText("Hello, Glad you could join us.")
    mbox.setDetailedText("Learn all you can about coding and join us.")
    mbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

    mbox.exec_()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(300, 300)
    w.setWindowTitle("Learn Code")

    label = QLabel(w)
    label.setText("Women Coders for life")
    label.move(100, 130)
    label.show()

    btn = QPushButton(w)
    btn.setText('Enter')
    btn.move(110, 150)
    btn.show()
    btn.clicked.connect(dialog)

    w.show()
    sys.exit(app.exec_())