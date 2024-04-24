# Assignment 5, Task 5
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 4:00 hrs
from typing import List
def word_sleuth(grid: List[List[str]], words: List[str]):
    ans = []
    r = 0
    s = ''
    ss = []
    for i in grid:
        for j in i:
            ss.append(j)
    print(ss)
print(word_sleuth(
[["r","a","w","b","i","t"],
["x","a","y","z","c","h"],
["p","q","b","e","i","e"],
["t","r","s","b","o","g"],
["u","w","x","v","i","t"],
["n","m","r","w","o","t"]]
,["bog", "moon", "rabbit", "the", "bit", "raw"]
))
