# Assignment 4, Task 5
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 1:00 hrs
from typing import List
def allMultiplesOfK(k: int, lst: List[int]) -> bool:
    total = 0
    for i in lst:
        total += i
    if total%k == 0:
        return True
    else:
        return False
# print(allMultiplesOfK(4,[1,10,20]))
# print(allMultiplesOfK(3, [81,3,24]))
# print(allMultiplesOfK(11, []))