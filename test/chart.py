from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import platform


class window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitWindow()

    def InitWindow(self):
        def paintEvent(self):
            painter = QPainter(self)
            painter.drawText(400, 400, "5")
            rectpainter = QRect(100, 100, 100, 100)
            painter.drawRect(rectpainter)
            painter.drawText(rectpainter, Qt.AlignCenter, "5")

        self.setGeometry(1000, 1000, 1000, 1000)

        scene = QGraphicsScene()
        redBrush = QBrush(Qt.darkRed)
        blackPen = QPen(Qt.black)
        blackPen.setWidth(3)

        rect = scene.addRect(10, 10, 100, 100, blackPen, redBrush)

    def paintText(self):
        painter = QPainter(self)
        painter.drawText(100, 100, "5")

        text1 = scene.addText("5", QFont("Sanserif", 11))

        view = QGraphicsView(scene, self)

        view.setGeometry(0, 0, 680, 500)

        self.show()


app = QApplication(sys.argv)
window = window()
app.exec_()
