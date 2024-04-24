# Assignment 5, Task 4
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 4:00 hrs
log_book = [
"cycling;time:1,49;distance:2",
"jogging;time:40,11;distance:6",
"swimming;time:1,49;distance:1.2",
"jogging;time:36,25;distance:5.3",
"hiking;time:106,01;distance:8.29"
]
from typing import List
def jogging_average(activities: List[str]) -> float:
    Jog = []
    jog = []
    Time = []
    Dis = []
    Ntime = []
    Ndis = []
    NNtime = []
    total_time = 0
    total_dis = 0.0
    for i in log_book:
        if i[0:7] == 'jogging':
            Jog.append(i)
    for i in Jog:
        jog.append(i.split(';'))
    for i in jog:
        Dis.append(i[2])
        Time.append(i[1])
    for i in Dis:
        Ndis.append(i[9:])
    for i in Time:
        Ntime.append(i[5:])
    for i in Ntime:
        NNtime.extend(i.split(','))
    Time_int = list(map(int, NNtime))
    Dis_float = list(map(float, Ndis))
    for i in range(0, (len(Time_int)), 2):
        total_time = total_time + (Time_int[i] * 60) + (Time_int[i + 1])
    for i in Dis_float:
        total_dis = total_dis + i
    return ((total_dis * 1000) / total_time)

