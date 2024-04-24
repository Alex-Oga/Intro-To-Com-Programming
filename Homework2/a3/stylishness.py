# Assignment 3, Task 7
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 0:50 hrs
def got_table(you: int, date: int) -> str:
    if you<=2 or date<=2: # if you or the date have a value equal to or lower than 2, then it's a no
        return 'no'
    if you>=8 or date>=8: # if you or the date have a value equal to or higher than 8, then it's a yes
        return 'yes'
    else:
        return 'maybe' # Since both values are in between yes and no then the end result is maybe
assert got_table(7,3) == 'maybe'
assert got_table(9,4) == 'yes'
assert got_table(7,8) == 'yes'
assert got_table(1,10) == 'no'