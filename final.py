from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import platform

from PyQt5.uic import loadUiType
from Tools.demo.beer import n

CPU_Scheduler, _ = loadUiType('CPU_Scheduler.ui')


class MainApp(QMainWindow, CPU_Scheduler):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.ui = CPU_Scheduler
        self.handle_buttons()
        self.handle_line_edits()

    ############################################################
    # buttons connection to pages ##############################
    def handle_buttons(self):
        self.btn_1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
        self.btn_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.btn_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.btn_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))
        self.ok_2.clicked.connect(self.handle_line_edits)
        self.show()

    ############################################################
    # buttons connection to pages ##############################
    def handle_line_edits(self):
        n: int = self.process_no_2.text()
        print(n)

    ############################################################
    # fill data to the tables ##################################


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
