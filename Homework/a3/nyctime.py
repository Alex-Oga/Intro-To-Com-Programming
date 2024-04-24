# Assignment 3, Task 6
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 1:00 hrs
def nycHour(londonHour: int) -> str:
    time = londonHour-5
    if londonHour>=6 and londonHour<=16:
        return(f'{time}am')
    elif londonHour>6 or londonHour>16 and londonHour<=23:
        time = londonHour-5
        Time = time-12
        return(f'{Time}pm')
    elif londonHour == 0:
        time = 24-5
        Time = time-12
        return(f'{Time}pm')
    elif londonHour == 5:
        time = 12
        return(f'{time}am')
nycHour(12)