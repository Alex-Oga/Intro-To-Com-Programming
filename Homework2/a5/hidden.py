# Assignment 5, Task 2
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 4:00 hrs
def is_hidden(s, t):
    total = 1
    if t[0] in s and t[-1] in s:
        for i in t:
            newStr = s[s.index(t[0]):s.rindex(t[-1]) + 1]
            if i in newStr:
                pass
            else:
                return False
        for i in range(len(t)-1):
            if s.index(s[i])<s.index(s[i+1]):
                total += 1
                if total == len(t):
                    return True
            else:
                return False
    else:
        return False
# print(is_hidden("welcometothehotelcalifornia","melon"))
# assert is_hidden("welcometothehotelcalifornia","space") == False
# assert is_hidden("TQ89MnQU3IC7t6","MUIC") == True
# assert is_hidden("VhHTdipc07","htc") == False
# assert is_hidden("VhHTdipc07","hTc") == True