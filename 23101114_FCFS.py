pid = ["p4", "p2", "p1", "p3", "p5"]
AT = [1, 2, 3, 4, 5]
BT = [2, 4, 5, 3, 3]
CT = []
TAT = []
WT = []
ct = 0
for i in range(5):
    if ct < AT[i]:
        ct = AT[i]
    ct = ct + BT[i]
    CT.append(ct)
for i in range(5):
    tat = CT[i] - AT[i]
    TAT.append(tat)
    wt = tat - BT[i]
    WT.append(wt)
avg_tat = sum(TAT) / 5
avg_wt = sum(WT) / 5