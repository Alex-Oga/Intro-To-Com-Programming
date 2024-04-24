# Assignment 5, Task 1
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 4:00 hrs
from typing import List
def loveTri(n: int) -> List[List[int]]:
    lst = [1]
    newlst = [lst]
    for i in range(n):
        ls = [newlst[-1][-1]]
        for j in range(i):
            ls.append(newlst[-1][j]+ls[j])
        newlst.append(ls)
    return newlst[1:]
# print(loveTri(5))
