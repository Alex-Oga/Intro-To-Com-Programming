from typing import List
def place_me(L:List[int], x:int) -> List[int]:
    L.append(x)
    L.sort()
    return L
print(place_me([4,12,1,13],5))
def place_me_v0(L:List[int], x:int) -> List[int]:
    index: int = 0
    copy_L = L[:]
    while index < len(L) and L[index] < x:
        index += 1
    copy_L.insert(index,x)
    return copy_L
print(place_me_v0([1,2,3],5))
def sum_even(n:int):
    total = 0
    for i in range(1,n,1):
        if i%2 == 0:
            total += i
    return total
print(sum_even(1000001))
def sum_e():
    total = 0
    for i in range(1,1000001,1):
        if i%2 == 0:
            total += i
    return total
print(sum_e())
print(0,end=' ')
print(1,end=' ')
for row in range(3):
    start = row%2
    print(start,end=' ')
    print(start+1, end=' ')
    print(start,end=' ')
print()
n_col = 8
n_row = 10
for row in range(n_row):
    start = row%2
    for col in range(n_col):
        print(start,end=' ')
        if start == 0:
            start = 1
        else:
            start = 0
    print()
