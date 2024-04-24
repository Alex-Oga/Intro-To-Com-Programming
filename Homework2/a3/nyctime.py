# Assignment 3, Task 6
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 1:00 hrs
def nycHour(londonHour: int) -> str:
    timeDifference = 5 # Difference of time between New York and London
    if londonHour<=4:
        return (f'{7+londonHour}pm')
    if londonHour == 5:
        return '12am'
    if 6<=londonHour<=16:
        return (f'{londonHour-timeDifference}am') # Subtracting between 6 and 16 leaves the remainder in am time
    if londonHour == 17:
        return '12pm'
    if 18<=londonHour<=23:
        return (f'{londonHour-12-timeDifference}pm') # Subtracting between 18 and 23 leaves the remainder in pm time
# print(nycHour(0))
# assert(nycHour(1)) == '8pm'
# print(nycHour(2))
# print(nycHour(3))
# print(nycHour(4))
# print(nycHour(5))
# assert (nycHour(6)) == '1am'
# print(nycHour(7))
# print(nycHour(8))
# print(nycHour(9))
# print(nycHour(10))
# print(nycHour(11))
# print(nycHour(12))
# print(nycHour(13))
# print(nycHour(14))
# print(nycHour(15))
# print(nycHour(16))
# print(nycHour(17))
# print(nycHour(18))
# print(nycHour(19))
# print(nycHour(20))
# print(nycHour(21))
# print(nycHour(22))
# print(nycHour(23))
# assert nycHour(0) == '7pm'
# assert nycHour(11) == '6am'
# assert nycHour(23) == '6pm'
# assert nycHour(17) == '12pm'
# assert nycHour(5) == '12am'