# Assignment 7, Task 1
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 4:00 hrs
from itertools import permutations
from typing import Set
from typing import Tuple
def all_perm(n: int) -> Set[Tuple[int, ...]]:
    lst = []
    lstList = []
    i = 0
    while i<n:
        i = i+1
        lst.append(i)
    p = permutations(lst, n)
    for i in list(p):
        lstList.append(i)
    return set(lstList)
