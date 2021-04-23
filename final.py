from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import platform

from PyQt5.uic import loadUiType
CPU_Scheduler, _ = loadUiType('CPU_Scheduler.ui')


class MainApp(QMainWindow, CPU_Scheduler):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.ui = CPU_Scheduler
        self.handle_buttons()

    ###########################################################
    # buttons connection to pages ##############################
    def handle_buttons(self):
        self.btn_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_1))
        self.btn_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_2))
        self.btn_3.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_3))
        self.btn_4.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.page_4))
        self.show()


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
