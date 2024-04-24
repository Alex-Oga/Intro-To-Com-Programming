# Assignment 7, Task 3
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 4:00 hrs
class DataFrame:
    def __init__(self):
        self.ans = []
    def add(self, x):
        if type(x) != list:
            self.ans.append(x)
        else:
            for i in x:
                self.ans.append(i)
    def mean(self):
        total = 0
        for i in self.ans:
            total += i
        return total/len(self.ans)
    def percentile(self, r):
        length = len(self.ans)
        return self.ans[int((r*0.01)*length):]
    def mode(self):
        dct = dict()
        lst = []
        an = []
        for i in self.ans:
            dct[i] = 0
        for i in self.ans:
            dct[i] += 1
        for i in dct.values():
            lst.append(i)
        for i in dct:
            if dct[i] == max(lst):
                an.append(i)
        return an
    def sd(self):
        pass
# data = DataFrame()
# data.add([1,2,3,4,5,6,7,8])
# print(data.mean())
# print(data.mode())
# print(data.percentile(98))