class ProcessCame:
	arrival_time = int(0)
	burst_time = int(0)
	matchSlice = int(0)
	Process_name = " "


class ProcessEnd:
	waiting_time = int(0)
	turnArround_time = int(0)
	process_name = " "


class WaitingQueue:
	process = ProcessCame()
	exit_time = int(0)


arrPC = ProcessCame()
arrPC = []
countPC = 0
pointerPC = 0

arrPE = ProcessEnd()
arrPE = []

arrRun = ProcessCame()
arrRun = []
countRun = 0
pointerRun = 0

arrAux = ProcessCame()
arrAux = []
countAux = 0
pointerAux = 0

arrWQ = WaitingQueue()
arrWQ = []
countWQ = 0
pointerWQ = 0

timeSlice = 0
timeWQ = 0
remainQueue = 0

i = 0
total = input("Enter The Number of Processes: ")
total = int(total)
timeSlice = input("Enter the Time Slice: ")
timeSlice = int(timeSlice)
timeWQ = input("Time for I/O : ")
timeWQ = int(timeWQ)
remainQueue = input("Time to stay in Waiting Queue: ")
remainQueue = int(remainQueue)
#loop = total
while i < total:
	temp = ProcessCame()
	temp.Process_name = input("Enter a Process Name: ")
	temp.arrival_time = input("Enter the Arrival time: ")
	temp.arrival_time = int(temp.arrival_time)
	temp.burst_time = input("Enter the Burst time: ")
	temp.burst_time = int(temp.burst_time)
	temp.matchSlice = 0
	arrPC.append(temp)
	countPC += 1
	i += 1


sort1 = 0
sort2 = 0

while sort1 < total:
	sort2 = 0
	while sort2 < total - 1:
		if arrPC[sort2].arrival_time > arrPC[sort2 + 1].arrival_time:
			temp = ProcessCame()
			temp.arrival_time = arrPC[sort2].arrival_time
			temp.burst_time = arrPC[sort2].burst_time
			temp.Process_name = arrPC[sort2].Process_name
			arrPC[sort2].arrival_time = arrPC[sort2 + 1].arrival_time
			arrPC[sort2].burst_time = arrPC[sort2 + 1].burst_time
			arrPC[sort2].Process_name = arrPC[sort2 + 1].Process_name
			arrPC[sort2 + 1].arrival_time = temp.arrival_time
			arrPC[sort2 + 1].burst_time = temp.burst_time
			arrPC[sort2 + 1].Process_name = temp.Process_name
		sort2 += 1
	sort1 += 1

burst = []

p = 0
while p < total:
	burst.append(arrPC[p].burst_time)
	p += 1

aflag = 0
j = 0
while pointerRun < countRun or pointerPC < countPC or pointerWQ < countWQ or pointerAux < countAux:
	if pointerPC < countPC and j == arrPC[pointerPC].arrival_time:
		arrRun.append(arrPC[pointerPC])
		pointerPC += 1
		countRun += 1
	if countRun == 0 or pointerRun - 1 == countRun:
		j += 1
	else:
		if pointerRun < countRun and (pointerAux == countAux - 1 or countAux == 0):
			arrRun[pointerRun].burst_time -= 1
			arrRun[pointerRun].matchSlice += 1
			aflag = 0
		else:
			if pointerAux < countAux:
				arrAux[pointerAux].burst_time -= 1
				arrAux[pointerAux].matchSlice += 1
				aflag = 1
		if (pointerRun < countRun and arrRun[pointerRun].burst_time == 0) or (pointerAux < countAux and arrAux[pointerAux].burst_time == 0):
			if aflag == 0:
				temp = ProcessEnd()
				temp.process_name = arrRun[pointerRun].Process_name
				temp.turnArround_time = (j - arrRun[pointerRun].arrival_time) + 1
				# print(arrRun[pointerRun].burst_time)
				o = 0
				while o < total:
					if temp.process_name == arrPC[o].Process_name:
						temp.waiting_time = temp.turnArround_time - burst[o]
					o += 1
				# temp.waiting_time = temp.turnArround_time
				arrPE.append(temp)
				pointerRun += 1
			else:
				temp = ProcessEnd()
				temp.process_name = arrAux[pointerAux].Process_name
				temp.turnArround_time = (j - arrAux[pointerAux].arrival_time) + 1
				# print(arrRun[pointerRun].burst_time)
				o = 0
				while o < total:
					if temp.process_name == arrPC[o].Process_name:
						temp.waiting_time = temp.turnArround_time - burst[o]
					o += 1
				# temp.waiting_time = temp.turnArround_time
				arrPE.append(temp)
				pointerAux += 1
				if pointerAux == countAux - 1:
					aflag = 0
		else:
			if pointerRun < countRun and arrRun[pointerRun].matchSlice == timeWQ:
				temp = WaitingQueue()
				temp.process = arrRun[pointerRun]
				temp.exit_time = j + remainQueue
				arrWQ.append(temp)
				countWQ += 1
				pointerRun += 1
			else:
				if pointerRun < countRun and arrRun[pointerRun].matchSlice == timeSlice:
					arrRun.append(arrRun[pointerRun])
					pointerRun += 1
					countRun += 1
		if pointerWQ < countWQ and arrWQ[pointerWQ].exit_time == j:
			arrAux.append(arrWQ[pointerWQ].process)
			pointerWQ += 1
			countAux += 1
		j += 1


l = 0
while l < total:
	#print(arrPC[l].arrival_time,arrPC[l].Process_name,arrPC[l].burst_time)
	print(arrPE[l].turnArround_time, arrPE[l].process_name, arrPE[l].waiting_time)
	l += 1n