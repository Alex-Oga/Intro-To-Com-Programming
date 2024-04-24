# Assignment 4, Task 2
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 0:30 hrs
def powerLoop(upto: int) -> None:
    for i in range(upto+1):
        print(i,end=' ')
        print((11**i)%101)
# print(powerLoop(3))