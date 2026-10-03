processes = ["P1", "P2", "P3", "P4"]
arrival_time = [0, 1, 3, 2]
burst_time = [4, 2, 2, 1]
remaining_time = burst_time.copy()
completion_time = [0] * 4
waiting_time = [0] * 4
turnaround_time = [0] * 4
time = 0
completed = 0
while completed < 4:
    idx = -1
    shortest = 9999
    for i in range(4):
        if arrival_time[i] <= time and remaining_time[i] > 0:
            if remaining_time[i] < shortest:
                shortest, idx = remaining_time[i], i
    if idx == -1:
        time += 1
        continue
    remaining_time[idx] -= 1
    time += 1
    if remaining_time[idx] == 0:
        completion_time[idx] = time
        completed += 1