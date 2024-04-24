# Assignment 4, Task 7
# Name: Alexander Ogay
# Collaborators:
# Time Spent: :00 hrs
def is_prime(n: int)-> bool:
    if n >= 2:
        for i in range(2, n):
            if (n % i) == 0:
                return False
                break
            else:
                return True
                break
    else:
        return False
is_prime(41)
from typing import List
def sans_primes(numbers: List[int])-> List[int]:
    index = 0
    new_list = []
    for i in numbers:
        if (numbers[index] % i) == 0:
            new_list.append(numbers[index])
        else:
            break
        index = index + 1
    return(new_list)
sans_primes([1,4,9,10])