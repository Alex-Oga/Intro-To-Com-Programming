# Assignment 5, Task 4
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 4:00 hrs
from typing import List
def jogging_average(activities: List[str]) -> float:
    totalTime = 0
    totalDistance = 0
    for i in activities:
        x,y,z = i.split(';') # Split the activity, time and distance
        if x == 'jogging': # To only get data from jogging
            a,b = y.split(':') # Split time from the numbers
            c,d = b.split(',') # Split the minutes from time
            totalTime += (int(c)*60)+int(d) # Convert minutes to seconds and add the seconds
            e,f = z.split(':') # Split distance from the numbers
            totalDistance += float(f)*1000 # Multiply distance by 1000 to get meters
    return totalDistance/totalTime
# log_book = [
# "cycling;time:1,49;distance:2",
# "jogging;time:40,11;distance:6",
# "swimming;time:1,49;distance:1.2",
# "jogging;time:36,25;distance:5.3",
# "hiking;time:106,01;distance:8.29"
# ]
# print(jogging_average(log_book))