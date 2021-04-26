from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import platform
import FCFS
from FCFS import *
import Shortest_Job_First
from Shortest_Job_First import *

from PyQt5.uic import loadUiType

CPU_Scheduler, _ = loadUiType('CPU_Scheduler.ui')


class MainApp(QMainWindow, CPU_Scheduler):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.onlyInt = QIntValidator()
        self.setupUi(self)
        self.ui = CPU_Scheduler
        self.restrict_input()
        self.handle_buttons()

    ###########################################################
    # buttons connection to pages ##############################
    def handle_buttons(self):
        self.btn_1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
        self.btn_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.btn_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.btn_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))
        self.ok_1.clicked.connect(lambda: self.handle_line_edits_1())
        self.ok_2.clicked.connect(lambda: self.handle_line_edits_2())
        self.ok_3.clicked.connect(lambda: self.handle_line_edits_3())
        self.ok_4.clicked.connect(lambda: self.handle_line_edits_4())
        self.simulate_1.clicked.connect(lambda: self.simulate_1_handler())
        self.simulate_2.clicked.connect(lambda: self.simulate_2_handler())
        self.simulate_3.clicked.connect(lambda: self.chart3())
        self.simulate_4.clicked.connect(lambda: self.chart4())

        self.show()

    ############################################################
    # no of process variables connection to line edits ##############################
    def handle_line_edits_1(self):
        FCFS.n1 = int(self.process_no_1.text())
        self.tableWidget_1.setRowCount(int(FCFS.n1))

    def handle_line_edits_2(self):
        Shortest_Job_First.N = int(self.process_no_2.text())
        self.tableWidget_2.setRowCount(int(Shortest_Job_First.N))
        Shortest_Job_First.preemptive = self.preemptive_1.isChecked()

    def handle_line_edits_3(self):
        n3: int = self.process_no_3.text()
        print(n3)
        # self.tableWidget_3.setRowCount(int(n3))

    def handle_line_edits_4(self):
        n4: int = self.process_no_4.text()
        print(n4)
        # self.tableWidget_4.setRowCount(int(n4))

    def restrict_input(self):
        self.process_no_1.setValidator(self.onlyInt)
        self.process_no_2.setValidator(self.onlyInt)
        self.process_no_3.setValidator(self.onlyInt)
        self.process_no_4.setValidator(self.onlyInt)

    def simulate_1_handler(self):
        # inputs
        for i in range(int(FCFS.n1)):
            arrival = self.tableWidget_1.item(i, 1).text()
            burst = self.tableWidget_1.item(i, 2).text()
            p = Process(i + 1, arrival, burst)
            inputQueue.put(p)
        # output
        simulate_fcfs()
        self.chart1()

    def simulate_2_handler(self):
        # inputs
        for i in range(int(Shortest_Job_First.N)):
            arrival = self.tableWidget_2.item(i, 1).text()
            burst = self.tableWidget_2.item(i, 2).text()
            Shortest_Job_First.processes.append([float(arrival), float(burst), "P" + str(i + 1), 0])
            Shortest_Job_First.cprocesses.append([float(arrival), float(burst), "P" + str(i + 1), 0])
            # output
        simulate_sjf()
        self.chart2()

    ############################################################
    # Gantt chart ##################################
    def chart1(self):
        scene = QGraphicsScene()
        whiteBrush = QBrush(Qt.white)
        redPen = QPen(Qt.darkRed)
        redPen.setWidth(3)

        # draw
        f = 860 / FCFS.totalBurstTime  # drawing factor
        time = 0.0
        for s in list(outputQueue.queue):
            rect = scene.addRect(time * f, 50, s[1] * f, 40, redPen, whiteBrush)
            time += s[1]
            item = scene.addText("P" + str(s[0]), QFont('Arial', 13))
            item.setPos((time - (s[1] / 2)) * f - 7, 57)
            item = scene.addText(str(time), QFont('Arial', 11))
            item.setPos(time * f - 12, 100)

        # avgWaitingTime = totalWaitingTime / int(n1)
        # print(avgWaitingTime)        

        self.graphicsView_1.setScene(scene)
        self.graphicsView_1.show()

    def chart2(self):
        # test
        print("test2")
        pass

    def chart3(self):
        # test
        print("test3")

    def chart4(self):
        # test
        print("test4")


def main():
    FCFS.init()
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
