# Assignment 3, Task 1
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 0:40 hrs
def my_min (p: float, q: float, r: float)-> float:
    if p < q and p < r:
        return p
    elif q < p and q < r:
        return q
    elif r< q and r<p:
        return r

def my_mean(p: float, q: float, r: float)-> float:
    sum = p+q+r
    sum = sum/3
    return sum

def my_med(p: float, q: float, r: float) -> float:
    if p<r and p>q or p>r and p<q:
        return p
    elif r<q and r>p or r>q and r<p:
        return r
    elif q<p and q>r or q>p and q<r:
        return q

my_min(3.0,1.0,9.0)
my_mean(3.0, 7.0, 4.0)
my_med(4.0,1.0,5.0)