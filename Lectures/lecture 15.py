from typing import Set
B: Set[int] = {1, 2, 3}
C: Set[str] = {'a','b','c'}
#Empty Set
#Set has no duplicates, doesnt accept anything mutable
E: Set[int] = set()
#not{}
#Indexing and Slicing doesnt work on set
lst = [1,2,3,4]
S = set(lst)
print(S)
CharSet = set('abc')
print(CharSet)
print(len(CharSet))
#insert into set, List cannot be inserted
s = set()
s.add((1,3,4,5))
print(s)
#membership testing
A = {1,2,3}
B = {3,4,5}
print(1 in A)
print(10 in A)
print('A-B',A - B)
print(A == B)
print(A>B)
from typing import List
def unique(lst:List[int]):
    print(set(lst))
unique([1,2,3,4,4,4])
def fpp(L1,L2):
    ans = []
    for i in L1:
        if i not in L2:
            ans.append(i)
    for i in L2:
        if i not in L1:
            ans.append(i)
    print(ans)
fpp([1,2,3,4,5],[2,4,6,8])
# A set is a collection of distinct objects
# a = {1,2,3}
# b = {2}
# b is a subset of a
# a is a superset of b
# A|B, A Union B
# A&B, A intersect B
# A-B, A\B
