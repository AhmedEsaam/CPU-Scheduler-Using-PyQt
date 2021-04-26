global N
global preemptive
global cpu
cpu = []
global os
os = 0.0
global Average
Average = 0.0
global processes
processes = []
global cprocesses
cprocesses = []

def simulate_sjf():
    global cpu
    global os
    global Average
    processes.clear
    cprocesses.clear
    if (preemptive):
        os = 0
        cpu.clear()

        processes.sort()
        cprocesses.sort()
        os = processes[0][0]
        i = 0
        while 1:
            j = 0
            while j < int(N):
                if os < processes[j][0]:
                    break
                j += 1
            x = []
            for a in range(0, j):
                if processes[a][1] != 0:
                    x.append([processes[a][1], processes[a][2]])
            if x.__len__() == 0:
                break
            x.sort()

            temp = os
            temp += x[0][0]
            j = 0
            while j < int(N):
                if temp < processes[j][0]:
                    break
                j += 1
            y = []

            for a in range(0, j):
                if processes[a][1] != 0 and (processes[a][0] > os and processes[a][2] != x[0][1]):
                    y.append([processes[a][0], processes[a][1], processes[a][2]])

            y.sort()
            l = 0
            while 1:
                if y.__len__() == 0:
                    break
                if y[0][2] == processes[l][2]:
                    break
                l += 1

            if y.__len__() != 0:
                if y[0][1] < (temp - processes[l][0]):
                    cpu.append([processes[l][0] - os, x[0][1]])
                    os = processes[l][0]
                    k = 0
                    while 1:
                        if x[0][1] == processes[k][2]:
                            print(processes[k][2])
                            processes[k][1] = temp - processes[l][0]
                            break
                        k += 1

                else:
                    t = 0
                    c = y.__len__()
                    while c != 0:
                        c -= 1

                        if y[t][1] < (temp - y[t][0]):
                            cpu.append([y[t][0] - os, x[0][1]])
                            os = y[t][0]
                            k = 0

                            while 1:
                                if x[0][1] == processes[k][2]:
                                    processes[k][1] = temp - y[t][0]
                                    min = processes[k][1]
                                    break
                                k += 1
                            break

                        if c == 0:
                            os = temp
                            cpu.append(x[0])

                            k = 0
                            while 1:
                                if x[0][1] == processes[k][2]:
                                    processes[k][1] = 0
                                    cprocesses[k][3] = os - \
                                        cprocesses[k][1] - cprocesses[k][0]
                                    break
                                k += 1
                            break
                        t += 1

            else:
                os = temp
                cpu.append(x[0])

                k = 0
                while 1:
                    if x[0][1] == processes[k][2]:
                        processes[k][1] = 0
                        cprocesses[k][3] = os - cprocesses[k][1] - cprocesses[k][0]
                        break
                    k += 1
        Average = 0
        for i in range(int(N)):
            Average += cprocesses[i][3]

        Average /= int(N)
        print("Average waiting time = " + str(Average))
        print(cpu)
        print(os)

    else:
        os = 0
        cpu.clear()

        processes.sort()
        os = processes[0][0]
        i = 0
        while 1:
            j = 0
            while j < int(N):
                if os < processes[j][0]:
                    break
                j += 1
            x = []
            for a in range(0, j):
                if processes[a][1] != 0:
                    x.append([processes[a][1], processes[a][2]])
            if x.__len__() == 0:
                break
            x.sort()
            os += x[0][0]
            cpu.append(x[0])

            k = 0
            while 1:
                if x[0] == [processes[k][1], processes[k][2]]:
                    processes[k][3] = os - processes[k][1] - processes[k][0]
                    processes[k][1] = 0

                    break
                k += 1

        Average = 0
        for i in range(int(N)):
            Average += processes[i][3]

        Average /= int(N)
        print("Average waiting time = " + str(Average))
        print(cpu)
        print(os)
