# Assignment 4, Task 3
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 4:00 hrs
def triangle(k: int) -> None:
    outPut = (2*k)-1
    if k == 1:
        print('*')
    if k>=2:
        for i in range(1,k+1):
            print(((outPut-(2*i-1))//2)*'#'+(2*i-1)*'*'+((outPut-(2*i-1))//2)*'#')
# print(triangle(3))
def diamond(k: int) -> None:
    outPut = (2 * k) + 1
    oldK = (2*k)-1
    half = (outPut+1)//2
    if k>= 2:
        for i in range(1,half):
            print(((outPut-(2*i-1))//2)*'#'+(2*i-1)*'*'+((outPut-(2*i-1))//2)*'#')
        for i in range(1,half):
            print(((outPut - (2 * i + 1)) // 2) * '#' + (2 * i + 1) * '*' + ((outPut - (2 * i + 1)) // 2) * '#')

# print(diamond(3))