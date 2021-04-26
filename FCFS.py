from queue import PriorityQueue
import queue

def init():
    global n1
    n1 = 0
    global totalBurstTime
    totalBurstTime = 0.0

class Process:
    def __init__(self, pid, arrival = 0, burst = 0):
        self.pid = int(pid)
        self.arrival = float(arrival)
        self.burst = float(burst)
        self.departure = 0.0

    def __lt__(self, other):
        return self.arrival < other.arrival

    def waitingTime(self):
        return self.departure - self.arrival - self.burst


inputQueue = PriorityQueue()
outputQueue = queue.Queue()
totalWaitingTime = 0.0

def simulate_fcfs():
    time = 0.0
        
    #output
    while not inputQueue.empty():
            p = inputQueue.get()
            time += p.burst
            p.departure = time
            global totalWaitingTime
            totalWaitingTime += p.waitingTime()
            outputQueue.put((p.pid, p.burst))

    global totalBurstTime
    totalBurstTime = time

    #print
    for n in list(outputQueue.queue):
        print(n)
    avgWaitingTime = totalWaitingTime / int(n1)
    print(avgWaitingTime)



















    



