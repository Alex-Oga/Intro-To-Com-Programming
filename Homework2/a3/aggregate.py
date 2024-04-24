# Assignment 3, Task 1
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 0:30 hrs
def my_min(p: float, q: float, r: float) -> float:
    if p<r and p<q: # Finding the lowest value of all the values
        return p
    if q<p and q<r:
        return q
    if r<p and r<q:
        return r
def my_mean(p: float, q: float, r: float) -> float:
    return ((p+q+r)/3) # add up all the numbers divide by how many there are
def my_med(p: float, q: float, r: float) -> float:
    if p>r and p<q or p<r and p>q: # Trying to find the middle value of the three values
        return p
    if q>p and q<r or q>r and q<p:
        return q
    if r>p and r<q or r>q and r<p:
        return r
# assert my_min(3.0,1.0,9.0) == 1.0
# assert my_mean(3.0,7.0,4.0) == (3+7+4)/3
# assert my_med(13.0,5.0,12.0) == 12.0