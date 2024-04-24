# Assignment 1, Task 5
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 0:20 hrs

### DO NOT REMOVE THIS PART ###

p: float = 10.2  # you may change the value to test your code
q: float = 15.0  # you may change the value to test your code

###############################

### Your code start here ######
# Combination of area_1 and area_3
# Area of a Circle: Pi*radius**2
circleArea = 3.14*(q/2)**2
# area_2
# Area of a rectangle: Length*Width
squareArea = p*q
# Combination of all 3 areas
totalArea = circleArea+squareArea
print('The total area is', totalArea)