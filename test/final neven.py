from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import platform

from PyQt5.uic import loadUiType

CPU_Scheduler, _ = loadUiType('CPU_Scheduler.ui')


class MainApp(QMainWindow, CPU_Scheduler):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.onlyInt = QIntValidator()
        self.setupUi(self)
        self.ui = CPU_Scheduler
        self.handle_buttons()
        self.restrict_input()
        self.paintEvent()

    ############################################################
    # buttons connections ##############################
    def handle_buttons(self):
        self.btn_1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
        self.btn_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.btn_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.btn_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))
        self.ok_1.clicked.connect(lambda: self.handle_line_edits)
        self.ok_2.clicked.connect(lambda: self.handle_line_edits)
        self.ok_3.clicked.connect(lambda: self.handle_line_edits)
        self.ok_4.clicked.connect(lambda: self.handle_line_edits)
        self.simulate_1.clicked.connect(lambda: self.chart1())
        self.simulate_2.clicked.connect(lambda: self.chart2())
        self.simulate_3.clicked.connect(lambda: self.chart3())
        self.simulate_4.clicked.connect(lambda: self.chart4())
        self.show()

    ############################################################
    # no of process variables connection to line edits ##############################
    def handle_line_edits(self):
        n1: int = self.process_no_1.text()
        # self.tableWidget_1.setRowCount(int(n1))
        n2: int = self.process_no_2.text()
        # self.tableWidget_2.setRowCount(int(n2))
        n3: int = self.process_no_3.text()
        # self.tableWidget_3.setRowCount(int(n3))
        n4: int = self.process_no_4.text()
        # self.tableWidget_4.setRowCount(int(n4))

    def restrict_input(self):
        self.process_no_1.setValidator(self.onlyInt)
        self.process_no_2.setValidator(self.onlyInt)
        self.process_no_3.setValidator(self.onlyInt)
        self.process_no_4.setValidator(self.onlyInt)

    ############################################################
    # Gantt chart ##################################
    def chart1(self):
        scene = QGraphicsScene()
        whiteBrush = QBrush(Qt.white)
        redPen = QPen(Qt.darkRed)
        redPen.setWidth(3)

        rect1 = scene.addRect(50, 50, 100, 100, redPen, whiteBrush)
        rect2 = scene.addRect(2000, 900, 100, 100, redPen, whiteBrush)
        text1 = scene.addText("20", QFont("Sanserif", 11))

        self.graphicsView_1.setScene(scene)
        self.graphicsView_1.show()

    def paintEvent(self):
        painter = QPainter(self)
        painter.drawText(400, 400, "5")
        rectpainter = QRect(100, 100, 100, 100)
        painter.drawRect(rectpainter)
        painter.drawText(rectpainter, Qt.AlignCenter, "5")

    def chart2(self):
        scene = QGraphicsScene()
        whiteBrush = QBrush(Qt.white)
        redPen = QPen(Qt.darkRed)
        redPen.setWidth(3)

        rect = scene.addRect(50, 50, 100, 100, redPen, whiteBrush)
        rect = scene.addRect(2000, 900, 100, 100, redPen, whiteBrush)

        self.graphicsView_2.setScene(scene)
        self.graphicsView_2.show()

    def chart3(self):
        scene = QGraphicsScene()
        whiteBrush = QBrush(Qt.white)
        redPen = QPen(Qt.darkRed)
        redPen.setWidth(3)

        rect = scene.addRect(50, 50, 100, 100, redPen, whiteBrush)
        rect = scene.addRect(2000, 900, 100, 100, redPen, whiteBrush)

        self.graphicsView_3.setScene(scene)
        self.graphicsView_3.show()

    def chart4(self):
        scene = QGraphicsScene()
        whiteBrush = QBrush(Qt.white)
        redPen = QPen(Qt.darkRed)
        redPen.setWidth(3)

        rect = scene.addRect(50, 50, 100, 100, redPen, whiteBrush)
        rect = scene.addRect(2000, 900, 100, 100, redPen, whiteBrush)

        self.graphicsView_4.setScene(scene)
        self.graphicsView_4.show()

    ############################################################
    # fill data to the tables ##################################


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
