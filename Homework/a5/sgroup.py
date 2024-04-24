# Assignment 5, Task 6
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 4:00 hrs
from typing import List
def separate(data: List[int], k: int) -> List[List[int]]:
    new_l = []
    x = len(data)/k
    z = round(x)
    q = 0
    for i in range(len(data)):
        new_l.append(data[q:z])
        q = q+z
        z = z+z
    return new_l
print(separate([10, 12, 45, 47, 91, 98, 99], 2))