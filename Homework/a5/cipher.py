# Assignment 5, Task 3
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 4:00 hrs
import math
def enc(msg: str, key: int) -> str:
    r = []*key
    rounded = len(msg)/key
    rounded: int = math.ceil(rounded)
    x = [r]*rounded
    n = 0
    m = key
    cur = 0
    s = ''
    for i in range(len(x)):
        x[cur] = msg[n:m]
        cur = cur + 1
        n = n+key
        m = m+key
    for k in range(key):
        for j in range(rounded):
            s = s+x[j][k]
            print(s)
enc("monosodium glutamate", 7)