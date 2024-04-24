# Assignment 7, Task 3
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 4:00 hrs
import collections
from typing import List
class DataFrame:
    def __init__(self, lst: List):
        self.lst = lst
    def add(self, x):
        self.x = x
        for i in x:
            self.lst.append(i)
        print(self.lst)
    def mean(self):
        total = 0
        count = 0
        for i in self.lst:
            total = total + i
            count = count+1
        print(total/count)
    def percentile(self, r):
        self.r = r
    def mode(self):
        d = collections.Counter(self.lst)
        d_list = dict(d)
        max_value = max(list(d.values()))
        mode_val = [num for num, freq in d_list.items() if freq == max_value]
        if len(mode_val) == len(self.lst):
            print("No mode")
        else:
            print(', '.join(map(str, mode_val)))
