# Assignment 4, Task 7
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 4:00 hrs
from typing import List
def is_prime(n: int) -> bool:
    total = 0
    if n>=2:
        for i in range(1,n+1,1):
            if n%i == 0:
                total +=1
        if total == 2: # If n is divided 2 (1 and itself) times then return True, else return False
            return True
        else:
            return False
    else:
        return False
# assert is_prime(1) == False
# assert is_prime(2) == True
# assert is_prime(-2) == False
# assert is_prime(5) == True
# assert is_prime(41) == True
# assert is_prime(323) == False
def sans_primes(numbers: List[int]) -> List[int]:
    total = 0
    newList = numbers
    for i in range(1,len(numbers)):
        if numbers[i-1]>=2:
            for j in range(numbers[0]):
                if numbers[0]%j == 0:
                    total += 1
                if total == 2:
                    del newList[i-1]
                    del newList[i]
    return newList
# print(sans_primes([1, 4, 9, 10]))