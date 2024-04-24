# Assignment 3, Task 8
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 4:00 hrs
def toRoman(n: int) -> str:
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000
    if n == I:
        return 'I'
    if n<=3:
        return 'I'*n
    if n == 4:
        return 'IV'
    if n == V:
        return 'V'
    if n<=8:
        return ('I'*(n-5))+'V'
    if n == 9:
        return 'IX'
    if n == X:
        return 'X'
    if n == L:
        return 'L'
    if n == C:
        return 'C'
    if n == D:
        return 'D'
    if n == M:
        return 'M'

