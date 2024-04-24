# Assignment 2, Task 5
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 0:20 hrs
# p: int = 7
# q: int = 5
# r: int = 3
# s: int = 12
lowest = min(p,q,r,s)
highest = max(p,q,r,s)
median: float = ((p+q+r+s)-(lowest+highest))/2
# Add all the numbers, subtract the highest and lowest, divide by 2 to get the median
print(median)