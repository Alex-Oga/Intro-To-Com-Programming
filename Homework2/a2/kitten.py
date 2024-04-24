# Assignment 2, Task 6
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 0:20 hrs
# hour: int = 22
# minute: int = 1
# meowing: bool = True
in_trouble: bool = hour<6 and meowing == True or hour>=22 and minute>0 and meowing == True
# if the hour is less than 6 or more than 22 and the cat is meowing then in_trouble is True else is False
print(in_trouble)