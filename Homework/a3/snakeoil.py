# Assignment 3, Task 2
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 0:30 hrs
def price(vol: int) -> float:
    if vol<10:
        snake = 17*vol
        cost = vol*20
        sum:float = snake+cost
        return sum
    elif vol>=10 and vol<=100:
        snake =17*vol
        cost = 500
        sum:float = snake+cost
        return sum
    elif vol>100:
        snake = 17*vol
        sum:float = snake*0.97
        return sum
price(200)