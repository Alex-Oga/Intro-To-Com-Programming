# Assignment 2, Task 4
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 1:00 hrs
# a: int = 20
# b: int = 10
d = (a+b)//2
smaller: int = d-(abs(a)-d)
# d - the difference between d and a or d and b == the higher number
bigger: int = d+(abs(a)-d)
# d + the difference between d and a or d and b == the higher number
print(smaller)
print(bigger)
