import sys
from UI import Circler
from PyQt5.QtWidgets import QApplication


if __name__ == '__main__':
    app = QApplication(sys.argv)
    circle = Circler()
    circle.show()
    sys.exit(app.exec())