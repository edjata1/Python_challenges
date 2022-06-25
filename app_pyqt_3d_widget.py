import sys
import requests

# Contains all modules needed to create GUI, QtWidgets module contains all major widgets
from PyQt5.QtWidgets import QApplication, QWidget
if __name__ == "__main__":
    # creating an object of the QApplication class
    # ENTRY POINT INTO APP: UI app must create an instance of QApplication
        # sys.argv: list of command-line parameters,
        # pass to the application when launching
        # no arguments passed, (USER): app = QApplication([]) or app = QApplication(sys.argv)
    app = QApplication(sys.argv)
    # make an object of the QWidget class.
    # (QWidget - Qt) base class of all UI objects,
    # app widget - dialogs, texts, buttons, bars, and so on
    # NEST widgets
    w = QWidget()
    # dimensions (px * px)
    w.resize(400, 400)
    # name app
    w.setWindowTitle("Q widget")

    # displays  widget on screen.
    w.show()
    # app.exec_() method: Qt/C++ event loop (parallel execution)
    sys.exit(app.exec_())