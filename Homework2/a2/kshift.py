# Assignment 2, Task 3
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 0:30 hrs
# st: str = 'meogalacitca'
# k: int = 2020
moveBy = k%len(st)
# Have the remainder of k be divided by the length of the string, so that the number that remains shows how many times.
# it is supposed to move by
shifted_st = st[moveBy*-1:]+st[:moveBy*-1]
# Slicing the number of times it is supposed to move by, off of the string and then flipping them around and joining them.
print(shifted_st)