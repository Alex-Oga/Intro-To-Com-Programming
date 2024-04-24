# Assignment 7, Task 1
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 4:00 hrs
from typing import Tuple
from typing import Set
def all_perm(n: int) -> Set[Tuple[int, ...]]:
    num = tuple()
    ans = set()
    for i in range(1,n+1):
        num += (i,)
    ans.add(num)
    print(ans)
all_perm(2)