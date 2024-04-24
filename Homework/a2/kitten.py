# Assignment 2, Task 6
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 0:30 hrs
hour: int = 6
minute: int = 55
safe = 23,1,2,3,4,5
meowing: bool = 22>=hour>6 and minute>=0 and hour!=safe or 6<=hour<22 and minute<=59 and hour!=safe
in_trouble: bool = (meowing)
print(in_trouble)