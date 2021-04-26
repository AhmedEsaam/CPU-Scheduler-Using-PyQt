from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
import platform
import ctypes
import FCFS
from FCFS import * 
import Shortest_Job_First
from Shortest_Job_First import * 
import Priority_sched
from Priority_sched import *
import RR_sched
from RR_sched import * 

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
        self.ok_1.setEnabled(False)
        self.ok_2.setEnabled(False)
        self.ok_3.setEnabled(False)
        self.ok_4.setEnabled(False)
        
    ###########################################################
    # buttons connection to pages ##############################
    def handle_buttons(self):
        self.btn_1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_1))
        self.btn_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_2))
        self.btn_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_3))
        self.btn_4.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_4))
        self.process_no_1.textChanged.connect(lambda: self.disable_ok())
        self.process_no_2.textChanged.connect(lambda: self.disable_ok())
        self.process_no_3.textChanged.connect(lambda: self.disable_ok())
        self.process_no_4.textChanged.connect(lambda: self.disable_ok())
        self.ok_1.clicked.connect(lambda: self.handle_line_edits_1())
        self.ok_2.clicked.connect(lambda: self.handle_line_edits_2())
        self.ok_3.clicked.connect(lambda: self.handle_line_edits_3())
        self.ok_4.clicked.connect(lambda: self.handle_line_edits_4())
        self.simulate_1.clicked.connect(lambda: self.simulate_1_handler())
        self.simulate_2.clicked.connect(lambda: self.simulate_2_handler())
        self.simulate_3.clicked.connect(lambda: self.simulate_3_handler())
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
        Priority_sched.N3 = int(self.process_no_3.text())
        self.tableWidget_3.setRowCount(int(Priority_sched.N3))
        Priority_sched.preemptive__2 = self.preemptive_2.isChecked()

    def handle_line_edits_4(self):
        RR_sched.n4 = int(self.process_no_4.text())
        self.tableWidget_4.setRowCount(int(RR_sched.n4))
        RR_sched.q = int(self.q_time.text())

############################################################
    # disable ok button if no text ##############################
    def disable_ok(self):
        self.ok_1.setEnabled(False)
        self.ok_2.setEnabled(False)
        self.ok_3.setEnabled(False)
        self.ok_4.setEnabled(False)
        if len(self.process_no_1.text()) > 0:
            self.ok_1.setEnabled(True)
        if len(self.process_no_2.text()) > 0:
            self.ok_2.setEnabled(True)
        if len(self.process_no_3.text()) > 0:
            self.ok_3.setEnabled(True)
        if len(self.process_no_4.text()) > 0 or len(self.q_time.text()) > 0:
            self.ok_4.setEnabled(True)

    def restrict_input(self):
        self.process_no_1.setValidator(self.onlyInt)
        self.process_no_2.setValidator(self.onlyInt)
        self.process_no_3.setValidator(self.onlyInt)
        self.process_no_4.setValidator(self.onlyInt)
        self.q_time.setValidator(self.onlyInt)


    def simulate_1_handler(self):
        try:
            #inputs
            for i in range(int(FCFS.n1)):
                arrival = self.tableWidget_1.item(i, 1).text()
                burst = self.tableWidget_1.item(i, 2).text()
                p = Process(i + 1, arrival, burst)
                inputQueue.put(p)
            #output
            simulate_fcfs()
            self.chart1()
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(0, "Please fill all data", "Error", 1)

    def simulate_2_handler(self):
        try:
            #inputs
            processes.clear()
            cprocesses.clear()
            for i in range(int(Shortest_Job_First.N)): 
                arrival = self.tableWidget_2.item(i, 1).text()
                burst = self.tableWidget_2.item(i, 2).text()
                Shortest_Job_First.processes.append([float(arrival),float(burst), (i+1),0]) 
                Shortest_Job_First.cprocesses.append([float(arrival),float(burst), (i+1),0]) 
            #output
            simulate_sjf()
            self.chart2()
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(0, "Please fill all data", "Error", 1)

    def simulate_3_handler(self):
        # try:
            #inputs
            for i in range(int(Priority_sched.N3)): 
                arrival = self.tableWidget_3.item(i, 1).text()
                priority = self.tableWidget_3.item(i, 2).text()
                burst = self.tableWidget_3.item(i, 3).text()
                Priority_sched.process.append({'arrival time' : float(arrival),'burst time' : float(burst),'process' : int(i+1),'priority' : int(priority)})
            #output
            simulate_pri()
            self.chart3()
        # except Exception as e:
        #     ctypes.windll.user32.MessageBoxW(0, "Please fill all data", "Error", 1)

    def simulate_4_handler(self):
        try:
            #inputs
            for i in range(int(RR_sched.n4)):
                arrival = self.tableWidget_4.item(i, 1).text()
                burst = self.tableWidget_4.item(i, 2).text()
                p = Process(i + 1, arrival, burst)
                inputQueue_RR.put(p)
            #output
            simulate_rr()
            self.chart4()
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(0, "Please fill all data", "Error", 1)


    ############################################################
    # Gantt chart ##################################

    #///////////////////////////////////////// Chart1 for FCFS /////////////////////////////////////
    def chart1(self):
        scene = QGraphicsScene()
        whiteBrush = QBrush(Qt.white)
        redPen = QPen(Qt.darkRed)
        redPen.setWidth(3)

        #draw
        f = 860 / FCFS.totalBurstTime  #drawing factor
        time = 0.0
        for s in list(outputQueue.queue):
            if(s['arrival'] > time):
                item = scene.addText(str(time), QFont('Arial', 11))
                item.setPos(time * f - 12, 100)
                time = s['arrival']
            
            rect = scene.addRect(time * f, 50, s['burst'] * f, 40, redPen, whiteBrush)
            #texts:
            item = scene.addText("P." + self.tableWidget_1.item(s['pid']-1, 0).text(), QFont('Arial', 13))
            item.setPos((time + (s['burst'] / 2)) * f - 7, 57)
            item = scene.addText(str(time), QFont('Arial', 11))
            item.setPos((time) * f - 12, 100)            

            time += s['burst']

        #last departure time text
        item = scene.addText(str(time), QFont('Arial', 11))
        item.setPos(time * f - 12, 100)
        
        self.graphicsView_1.setScene(scene)
        self.graphicsView_1.show()

        self.t_waiting_1.setText(str(FCFS.avgWaitingTime)+" ms")

    #///////////////////////////////////////// Chart2 or SJF /////////////////////////////////////
    def chart2(self):
        scene = QGraphicsScene()
        whiteBrush = QBrush(Qt.white)
        redPen = QPen(Qt.darkRed)
        redPen.setWidth(3)

        #draw
        f = 860 / Shortest_Job_First.os  #drawing factor
        time = 0.0
        for s in (Shortest_Job_First.cpu):
            rect = scene.addRect(time * f, 50, s[0] * f, 40, redPen, whiteBrush)
            #texts:
            item = scene.addText("P." + self.tableWidget_2.item(s[1]-1, 0).text(), QFont('Arial', 13))
            item.setPos((time + (s[0] / 2)) * f - 7, 57)
            item = scene.addText(str(time), QFont('Arial', 11))
            item.setPos((time) * f - 12, 100)            

            time += s[0]

        #last departure time text
        item = scene.addText(str(time), QFont('Arial', 11))
        item.setPos(time * f - 12, 100)
        
        self.graphicsView_2.setScene(scene)
        self.graphicsView_2.show()

        self.lbl_waitingtime_2.setText(str(Shortest_Job_First.Average)+" ms")

    #///////////////////////////////////////// Chart3 for Priority /////////////////////////////////
    def chart3(self):
        scene = QGraphicsScene()
        whiteBrush = QBrush(Qt.white)
        redPen = QPen(Qt.darkRed)
        redPen.setWidth(3)

        #draw
        f = 860 / Priority_sched.time  #drawing factor
        time = 0.0
        for s in (Priority_sched.OutputPriority):
            if(s['arrival'] > time):
                item = scene.addText(str(time), QFont('Arial', 11))
                item.setPos(time * f - 12, 100)
                time = s['arrival']
            rect = scene.addRect(time * f, 50, s['length'] * f, 40, redPen, whiteBrush)
            #texts:
            item = scene.addText("P." + self.tableWidget_3.item(s['process']-1, 0).text(), QFont('Arial', 13))
            item.setPos((time + (s['length'] / 2)) * f - 7, 57)
            item = scene.addText(str(time), QFont('Arial', 11))
            item.setPos((time) * f - 12, 100)            

            time += s['length']

        #last departure time text
        item = scene.addText(str(time), QFont('Arial', 11))
        item.setPos(time * f - 12, 100)
        
        self.graphicsView_3.setScene(scene)
        self.graphicsView_3.show()

        self.lbl_waitingtime_3.setText(str(Priority_sched.avg_waiting_time_pri)+" ms")

    #///////////////////////////////////////// Chart4 for RR ////////////////////////////////////
    def chart4(self):
        scene = QGraphicsScene()
        whiteBrush = QBrush(Qt.white)
        redPen = QPen(Qt.darkRed)
        redPen.setWidth(3)

        #draw
        f = 860 / RR_sched.totalBurstTime_RR  #drawing factor
        time = 0.0
        for s in list(outputQueue_RR.queue):
            if(s['arrival'] > time):
                item = scene.addText(str(time), QFont('Arial', 11))
                item.setPos(time * f - 12, 100)
                time = s['arrival']
            
            rect = scene.addRect(time * f, 50, s['burst'] * f, 40, redPen, whiteBrush)
            #texts:
            item = scene.addText("P." + self.tableWidget_4.item(s['pid']-1, 0).text(), QFont('Arial', 13))
            item.setPos((time + (s['burst'] / 2)) * f - 7, 57)
            item = scene.addText(str(time), QFont('Arial', 11))
            item.setPos((time) * f - 12, 100)            

            time += s['burst']

        #last departure time text
        item = scene.addText(str(time), QFont('Arial', 11))
        item.setPos(time * f - 12, 100)
        
        self.graphicsView_4.setScene(scene)
        self.graphicsView_4.show()

        self.lbl_waitingtime_4.setText(str(RR_sched.avgWaitingTime_RR)+" ms")



def main():
    FCFS.init()
    RR_sched.init()
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
