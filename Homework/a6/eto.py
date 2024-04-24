# Assignment 6, Task 4
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 4:00 hrs
from typing import List
def eto(lst: List[int]) -> List[int]:
    even = []
    odd = []
    for i in lst:
        if i%2 != 0:
            odd.append(i)
        else:
            even.append(i)
    ans = even+odd
    return ans
