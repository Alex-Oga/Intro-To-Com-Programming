# Assignment 6, Task 2
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 4:00 hrs
def passwordOK(password: str) -> bool:
    letters = set(('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'))
    upperLetters = set(('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'))
    specialSigns = set(('!','@','#','$','%'))
    numbers = set(('1','2','3','4','5','6','7','8','9','0'))
    newLst = []
    for i in password:
        newLst.append(i)
    newSet = set(newLst)
    if password.isupper() == True or password.islower() == True:
        return False
    if password.isdigit() == True or password.isalpha() == True:
        return False
    if len(password)<= 5 or len(password)>= 13:
        return False
    if newSet & letters != {} and newSet & upperLetters != {} and newSet & specialSigns != {} and newSet & numbers != {}:
        for i in range(0,len(password)-2,1):
            if password[i] == password[i+1]:
                if password[i] == password[i+1]:
                    return False
    return True
# print(passwordOK('ABd1234@1'))
# print(passwordOK('f#9'))
# print(passwordOK('Abbbc1!f'))
# print(passwordOK('nIc21!@!@!@!@'))