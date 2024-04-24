# Assignment 4, Task 5
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 0:30 hrs
from typing import List
def allMultiplesOfK(k: int, lst: List[int])-> bool:
    i = 0
    index = 0
    if lst == []:
        return(True)
    for i in lst:
        if lst[index] % k != 0:
            return(False)
            break
            index = index + 1
        else:
            return(True)
            break
allMultiplesOfK(4,[1,10,20])