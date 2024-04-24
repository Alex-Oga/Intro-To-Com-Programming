# Assignment 6, Task 3
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 4:00 hrs
from typing import List
from typing import Dict
def keepTabs(actions: List[str]) -> Dict[str, int]:
    names = []
    d:Dict[str,int] = dict()
    score = 0
    pos = +1
    neg = -1
    for i in actions:
        if i.endswith('+') == True:
            names.append(i.replace('++',''))
            d.update({i.replace('++',''):+1})
    for i in actions:
        if i.endswith('-') == True:
            names.append(i.replace('--',''))
            d.update({i.replace('--', ''): -1})
    for i in names:
        if names.count(i) == 2:
            names.remove(i)
    return d
keepTabs(["Jim++", "John--", "Jeff++", "Jim++", "John--", "John->Jeff",
"Jeff--", "June++", "Home->House"])