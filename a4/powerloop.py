# Assignment 4, Task 2
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 0:20 hrs
def powerLoop(upto:int)->None:
    if upto >= 0:
        result = (11**upto)%101
        print(upto,'',result)
        return None
powerLoop(1)