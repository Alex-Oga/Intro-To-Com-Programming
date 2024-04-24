# Assignment 3, Task 7
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 0:20 hrs
def got_table(you: int, date: int) -> str:
    if you>=8:
        return 'yes'
    elif date >= 8:
        return 'yes'
    elif you<=2:
        return 'no'
    elif date <= 2:
        return 'no'
    else:
        return 'maybe'

got_table(7,3)