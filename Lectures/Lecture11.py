"""
Topics covered so far:
 - Values & Expressions
 - Math expressions
 - Boolean expressions
 - Strings
 - Functions and unit tests
 - Conditional(if-elif-else)
 - Lists
 - For/While Loops
"""
"""
Assignment 2, Triangle
 - use abs(), because float is unreliable
"""
from typing import List
def readAloud(lst):
    ans = []
    count = 1
    for i in range(len(lst)-1):
        if lst[i] == lst[i+1]:
            count += 1
        else:
            ans.append(count)
            ans.append(lst[i])
            count = 1
    ans.append(count)
    ans.append(lst[-1])
    return ans
print(readAloud([1,1,3,2,1,1]))
def second_max(lst):
    m = max(lst)
    ans = min(lst)
    for each in lst:
        if each > ans and each < m:
            ans = each
    return ans
def kthDigit(x:int, b:int, k:int):
    return (x//(b**k))%b
def convertLetter(letter: str):
    letter = letter.lower()
    if letter in 'abc':
        return '2'
    elif letter in 'def':
        return '3'
    # ...
def phoneWord2Num(word:str):
    d0 = convertLetter(word[0])
    d1 = convertLetter(word[1])
    # ...
"""
Practice:
edabit.com
"""
def sans_primes2(numbers: List) -> List[int]:
    a = []
    if not isprime(numbers[0]):
        ans.append(numbers[0])
    for num in range(len(numbers)):
        if not isprime(numbers[i]) and not isprime(numbers[i-1]):
            ans.append(numbers[i])
    return ans