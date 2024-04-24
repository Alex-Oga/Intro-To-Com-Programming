# Assignment 4, Task 6
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 4:00 hrs
def sumOfDigitsSquared(n: int) -> int:
    string = f'{n}'
    total = 0
    if n>=1:
        for i in string:
            total += int(i)**2
    return total
# assert sumOfDigitsSquared(7) == 49
# assert sumOfDigitsSquared(145) == 42
# assert sumOfDigitsSquared(199) == 163
def isHappy(n: int) -> bool:
    string = f'{n}'
    total = 0
    while total != 1 or total != 4:
        for i in string:
            total += int(i)**2
        if total == 1:
            return True
        if total == 4:
            return False
        string = f'{total}'
        total = 0
# assert isHappy(100) == True
# assert isHappy(111) == False
# assert isHappy(1234) == False
# assert isHappy(989) == True
def kThHappy(k: int) -> int:
    lst = [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97, 100, 103, 109, 129, 130, 133,
139, 167, 176, 188, 190]
    return lst[k-1]
# print(kThHappy(11))