# Assignment 3, Task 2
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 0:30 hrs
def price(vol: int) -> float:
    cost = 17 # Cost of snake oil per litre
    litreShipping10 = 20 # The cost of shipping for orders less than 10 litres, per litre
    litreShipping10_100 = 500 # The cost of shipping for orders between 10 and 100
    discount = 3/100 # The discount for orders over 100 litres
    if vol<10:
        return float((vol*cost)+(vol*litreShipping10)) # Cost of oil + shipping
    if 10<=vol<=100:
        return float((vol*cost)+litreShipping10_100)
    if vol>100:
        return float(vol*cost)-(vol*cost*discount) # Cost of oil + discount
# assert price(5) == 185.0
# assert price(20) == 840.0
# assert price(200) == 3298.0
