# Assignment 4, Task 1
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 1:00 hrs
from typing import List
def altSum(lst: List[int]) -> int:
    if lst == []: # Makes sure function returns 0 if there is an empty list
        return 0
    total = lst[0] # Total starts from index 0 or else the for loop doesn't work
    for i in range(1,len(lst)): # for loop doesn't work if it starts from index 0 or if there is an empty list
        if i%2 == 0:
            total -= lst[i] # Alternating subtracting from sum
        else:
            total += lst[i] # Alternating adding to sum
    return total
# assert altSum([]) == 0
# assert altSum([1,3,5,2]) == 1
# assert altSum([7,7,7,7]) == 14
# assert altSum([31,4,28,5,71]) == -59
# assert altSum([1]) == 1