# Assignment 4, Task 3
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 1:00 hrs
def triangle(k: int)-> None:
    i = 1
    tri = 2 * k - 1
    trii = str(tri)
    triii = trii.replace(trii, '*')
    res = triii * tri
    slic = tri//2
    s = k - 1
    if k == 1:
        return(triii)
    elif k > 1:
        while i <= k:
            trsli = res[:slic]
            trsli2 = res[slic*-1:]
            sli1 = res.replace(trsli,'#')
            sli2 = sli1.replace(trsli2,'#')
            slic = slic + 1
            return(sli2)
            i = i + 1
            if i == k:
                return(res)
                break
triangle(3)
def diamond(k: int)-> None:
    i = 0
    l = 2*k
    d = 2*k+1
    d = d//2
    dia = '*'*d
    while i<=l:
        ddia = dia.replace(dia[:d],'#')
        ddia1 = ddia.replace(dia[d:],'#')
        i = i + 1
        return(ddia1)
diamond(2)