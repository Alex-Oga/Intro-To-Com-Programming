# Assignment 5, Task 3
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 4:00 hrs
def enc(msg: str, key: int) -> str:
    lst = []
    newStr = ''
    vertical = ((len(msg)*-1)//key)*-1
    for i in range(vertical):
        lst.append([msg[:key]])
        msg = msg[key:]
    print(lst)
    for i in range(vertical):
        for j in range(i):
            newStr += lst[j][i]
    return newStr
# print(enc('abc',2))