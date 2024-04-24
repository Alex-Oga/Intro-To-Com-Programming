# Assignment 6, Task 5
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 4:00 hrs
from typing import List
def mealCal(meal: List[str], recipes: List[str], db: List[str]) -> float:
    total = 0
    lst = []
    dct = dict()
    dc = dict()
    all = dict()
    menu = []
    for i in db:
        a,b = i.split(':')
        dct[a] = b
        all[a] = 0
    for i in recipes:
        a,b = i.split(':')
        dc[a] = b
    for i in meal:
        menu.append(dc[i])
    for i in menu:
        lst.append(i.split(','))
    for i in range(len(lst)):
        for j in lst[i]:
            a,b = j.split('*')
            all[a] += int(b)
    for i in all:
        a,b,c = dct[i].split(',')
        total += ((float(a)*4)+(float(b)*4)+(float(c)*9))*all[i]
    return total
# print(mealCal(["T-Bone", "T-Bone", "Green Salad1"],["Pork Stew:Cabbage*5,Carrot*1,Fatty Pork*10",
# "Green Salad1:Cabbage*10,Carrot*2,Pineapple*5",
# "T-Bone:Carrot*2,Steak Meat*1"],["Cabbage:4,2,0", "Carrot:9,1,5", "Fatty Pork:431,1,5",
# "Pineapple:7,1,0", "Steak Meat:5,20,10", "Rabbit Meat:7,2,20"]))