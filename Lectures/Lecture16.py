from typing import Dict
sid: Dict[str, float] = {'5680123':28.0,'5680345':30.0,'5680544':26.0}
sid['5680888'] = 10
for i in sid:
    print(i)
def find_avg(d):
    total = 0.0
    for stuid in d:
        total += d[stuid]
    return total/len(d)
print(find_avg(sid))

def tally(word: str):
    answer: Dict[str, int] = dict()
    for letter in word:
        answer[letter] = answer.get(letter,0) + 1
    return answer
print(tally("banana"))
# A dictionary is an unordered collection of key-value pairs
# Algorithm - An unambiguous specification of how to solve a class of problems
# AI - intelligence demonstrated by machines
# Bandwidth - Max rate of data transfer
# 1) Search up key
# 2) Add key-pair to dictionary
from typing import List, Tuple, Set, Dict
items = {'steak': 500, 'Lay': 20,'Apple': 50,'Chocolate': 15}
"""
Create a dictionary 
 - use {} to enclose items 
 - each item is separated by , 
 - each item contains a key and a value separated by :
"""
items['Pork'] = 200
del items['Apple']
ans: Dict[int,str] = {}
ans[999] = 'hello'
ans[654] = 'world'
d = {'a': 1, 'b': 2}
val = d.get('c',0)
print(val)
val = d.get('a')
print(val)
# Get all keys of a dictionary as a list
all_keys = list(items.keys())
print(all_keys)
# .values() returns a list-like collection of values
# IMPORTANT: do not rely on the order of keys and values returned from .keys() and .values()
scores: Dict[int, int] = {
    638947: 26,
    638948: 25,
    638273: 29
}
scores[620364] = 22
print(scores)
def find_avg(d:Dict[int,int]):
    total_sum = 0
    for each in d:
        total_sum += d[each]
    return total_sum/len(d)
print(find_avg(scores))
