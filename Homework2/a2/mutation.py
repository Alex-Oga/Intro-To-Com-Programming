# Assignment 2, Task 1
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 0:40 hrs
# s: str = 'HelloWorld!!'
# t: str = 'ThisIsPython'
# Step 1:
s = s.lower()# Convert s to lowercase
t = t.upper()# Convert t to uppercase
# Step 2: Replacing a,l,r into x
s = s.replace('a','x')
s = s.replace('l','x')
s = s.replace('r','x')
# Step 3: Replacing P,W,N into Z
t = t.replace('P','Z')
t = t.replace('W','Z')
t = t.replace('N','Z')
# Step 4:
new_s = s# Creating new string so that no errors come up when switching strings
new_t = t
new_s = new_s.replace(new_s[0],t[0],1)# Replacing first value of s with first value of t
new_t = new_t.replace(new_t[0],s[0],1)# Replacing first value of t with first value of s
# Step 5:
sMiddleThird = new_s[len(s)//3:((len(s)//3)*-1)]# First 1/3 of s to the last 1/3 of s,
# so that we can access the middle 1/3 of the string
tLastThird = new_t[len(t) - len(t)//3:]# Subtracting the length of the string by 1/3 so that we can get the last 1/3
new_s = new_s.replace(sMiddleThird,tLastThird,1)# Replacing middle 1/3 of s with last 1/3 of t
# Step 6:
z = new_s+new_t
print(z)