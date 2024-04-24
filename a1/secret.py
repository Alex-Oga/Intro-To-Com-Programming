# Assignment 1, Task 6
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 0:30 hrs

### DO NOT REMOVE THIS PART ###

# Update this variable to the last three digits
# of your student id *WITHOUT* leading 0's.
last_three: int = 727

###############################
M = 179424799**(17942-4691) + 373782901**(1548+5867)
# Last three digits of ID
k = last_three-1 # -1 because string count starts from 0 not 1
# Find first digit of secret code
b = (str(M)[::-1])[k] # reversed M and found the 727th position of the reversed string
# Find second digit of secret code
a = str(M)[k] # 727th position of string M
print('My secret code is',b+a)
