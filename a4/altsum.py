# Assignment 4, Task 1
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 1:40 hrs
from typing import List
def altSum(lst: List[int]):
    index = 0
    total = lst[0]
    st = 0
    llst = lst
    llst.pop(0)
    for i in llst:
        if st % 2 == 0:
            total = total + llst[index]
        else:
            total = total - llst[index]
        index = index + 1
        st = st + 1
    return(total)
altSum([1,2,5,3])