# Assignment 4, Task 4
# Name: Alexander Ogay
# Collaborators: Internet
# Time Spent: 1:00 hrs
from typing import List
from collections import Counter
def readAloud(lst: List[int])-> List[int]:
    lst.sort()
    i = 0
    index = 0
    lst2 = []
    print(Counter(lst))
    for i in lst:
        x = lst[index]
        lst2.append(lst.count(x))
        lst2.append(lst[index])
        index = index + 1
    return(lst2)
readAloud([1,2,-1,1])