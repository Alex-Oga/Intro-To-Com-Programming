# Assignment 5, Task 2
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 1:00 hrs
def is_hidden(s,t)->bool:
    S = set(s)
    T = set(t)
    if S&T == T:
        return True
    else:
        return False