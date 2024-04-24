# Assignment 6, Task 1
# Name: Alexander Ogay
# Collaborators:
# Time Spent: 4:00 hrs
n_string = ''
reader = open('text.txt.txt', 'r')
for line in reader:
    s_line = line.strip()
    st_line = s_line.lower()
    str_string = st_line.replace(' ', '')
    stri_string = str_string.replace('.','')
    strin_string = stri_string.replace(',','')
    n_string += strin_string
def charHistogram(filename: str) -> None:
    n = {}
    x = []
    total = 0
    for i in filename:
        filename.count(i)
        n.update({i: filename.count(i)})
    m = sorted(n, key=n.get, reverse=True)
    for i in n:
        x.append(n[i])
    x.sort(reverse=True)
    y = '+'
    for i in range(len(m)):
        print(m[i],x[i]*y)

print(charHistogram(n_string))