pid = ["P1", "P2", "P3", "P4", "P5"]
AT = [2, 3, 0, 1, 1]
BT = [5, 1, 2, 3, 6]
completed = [False] * 5
time, finished, sequence = 0, 0, []
while finished < 5:
    idx, min_bt = -1, 9999
    for i in range(5):
        if not completed[i] and AT[i] <= time and BT[i] < min_bt:
            min_bt, idx = BT[i], i
    if idx == -1:
        time += 1
    else:
        time += BT[idx]
        completed[idx] = True
        finished += 1
        sequence.append(pid[idx])