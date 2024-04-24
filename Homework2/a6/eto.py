# Assignment 6, Task 4
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 4:00
from typing import List
def eto(lst: List[int]) -> List[int]:
    evens = []
    odds = []
    for i in lst:
        if i%2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    newLst = evens+odds
    return newLst
# print(eto([3,1,2]))
# print(eto([4,2,8]))
# print(eto([8,-2,3,-3,-1,5,8,-1,5]))