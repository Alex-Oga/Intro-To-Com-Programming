a = 1
b = a
print(a,b)
a = 2
print(a,b)
c = [1,2]
d = c
print(c,d)
c[0] = 2
print(c,d)
e = [[1,2]]*3
f = e
print(f)
e[0][0] = 3
print(f)
g = [0]*3
h = [g]*2
print(h)
h[0][0] = 1
print(h)
i = [0]*3
j = [i[:]]*2
print(j)
j[0][0] = 1
print(j)
k = [[0]*3,[0]*3]
print(k)
k[0][0] = 1
print(k)
l = [0]*3
m = [l[:]]*2
print(m)
m[0][0] = 1
print(m)
n = 'cpa'
o =[7,1,1]
print(zip(n, o))
tup = zip(n, o)
for letter, valu in tup:
   print(letter, "->", valu)
from typing import List
lst: List[str] = ["emma", "jack", "caleb", "soph"]
for index, st in enumerate(lst):
    print(index, st)
lst: List[str] = ["emma", "jack", "caleb", "soph"]
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)
