# Assignment 6, Task 2
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 4:00 hrs
def passwordOK(password: str) -> bool:
    letters = 'abcdefghijklmnopqrstuvwxyz'
    upletters = letters.upper()
    num = '0123456789'
    specialchar = '$#@%!'
    minlength = 6
    maxlength = 12
    total = 0
    if len(set(password) & set(letters)) > 0 and len(set(password) & set(upletters)) > 0:
        if len(set(password) & set(num)) > 0 and len(set(password) & set(specialchar)) > 0:
            if len(password) >= minlength and len(password) <= maxlength:
                try:
                    for i in range(len(password)):
                        if password[i] == password[i + 1]:
                            total = total + 1
                            if total == 3:
                                return True
                            else:
                                return False
                        else:
                            total = 0
                except IndexError:
                    return True
            else:
                return False
        else:
            return False
    else:
        return False
