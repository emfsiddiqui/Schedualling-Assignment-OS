class ProcessCame:
	arrival_time = int(0)
	burst_time = int(0)
	Process_name = " "


class ProcessEnd:
	waiting_time = int(0)
	turnArround_time = int(0)
	process_name = " "


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



i = 0
total = input("Enter The Number of Processes: ")
total = int(total)
while i < total:
	temp = ProcessCame()
	temp.Process_name = input("Enter a Process Name: ")
	temp.arrival_time = input("Enter the Arrival time: ")
	temp.arrival_time = int(temp.arrival_time)
	temp.burst_time = input("Enter the Burst time: ")
	temp.burst_time = int(temp.burst_time)
	arrPC.append(temp)
	countPC += 1
	i += 1



check = 0
j = 0
while pointerRun < countRun or pointerPC < countPC:
	if pointerPC < countPC and j == arrPC[pointerPC].arrival_time:
		arrRun.append(arrPC[pointerPC])
		pointerPC += 1
		countRun += 1
	if countRun == 0 or pointerRun - 1 == countRun:
		j += 1
	else:
		if pointerRun < countRun:
			sort1 = pointerRun + 1
			sort2 = pointerRun + 1

			while sort1 < countRun:
				sort2 = pointerRun + 1
				while sort2 < countRun - 1:
					if arrPC[sort2].burst_time > arrPC[sort2 + 1].burst_time:
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
		check += 1
		if arrRun[pointerRun].burst_time == check:
			temp = ProcessEnd()
			temp.Process_name = arrRun[pointerRun].Process_name
			temp.turnArround_time = (j - arrRun[pointerRun].arrival_time) + 1
			#print(arrRun[pointerRun].burst_time)
			temp.waiting_time = temp.turnArround_time - arrRun[pointerRun].burst_time
			arrPE.append(temp)
			pointerRun += 1
			check = 0
		j += 1


l = 0
while l < total:
	#print(arrPC[l].arrival_time,arrPC[l].Process_name,arrPC[l].burst_time)
	print(arrPE[l].turnArround_time, arrPE[l].Process_name, arrPE[l].waiting_time)
	l += 1
