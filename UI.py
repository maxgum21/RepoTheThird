import random
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QPushButton, QWidget
from PyQt5.QtGui import QPainter, QPen, QColor


class Circler(QWidget):
    def __init__(self):
        super().__init__()
        self.p = False
        self.ui()

    def ui(self):
        self.setGeometry(200, 200, 500, 500)
        self.setWindowTitle('Кругляшки')

        self.drawBut = QPushButton('Нарисовать', self)
        self.drawBut.setGeometry(180, 380, 120, 70)
        self.drawBut.clicked.connect(self.draw)

    def paintEvent(self, event):
        if self.p:
            paint = QPainter()
            paint.begin(self)
            paint.setPen(QPen(Qt.black, 3, Qt.SolidLine))
            paint.setBrush(QColor(random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256)))
            radius1 = random.randrange(20, 200)
            radius2 = random.randrange(20, 200)
            paint.drawEllipse(100, 150, radius1, radius1)
            paint.setBrush(QColor(random.randrange(0, 256), random.randrange(0, 256), random.randrange(0, 256)))
            paint.drawEllipse(300, 150, radius2, radius2)
            paint.end()
            self.p = False

    def draw(self):
        self.p = True
        self.repaint()