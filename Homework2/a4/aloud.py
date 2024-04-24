# Assignment 4, Task 4
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 4:00 hrs
from typing import List
def readAloud(lst: List[int]) -> List[int]:
    newList = []
    ans = []
    for i in lst:
        if i not in newList:
            newList.append(i)
    for i in newList:
        ans.append(lst.count(i))
        ans.append(i)
    return ans
# assert readAloud([]) == []
# assert readAloud([1,1,1]) == [3,1]
# assert readAloud([-1,2,7]) == [1,-1,1,2,1,7]
# assert readAloud([3,3,8,-10,-10,-10]) ==  [2,3,1,8,3,-10]
# assert readAloud([3,3,1,1,3,1,1]) == [2,3,2,1,1,3,2,1]

