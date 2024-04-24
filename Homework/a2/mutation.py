# Assignment 2, Task 1
# Name: Alexander Ogay
# Collaborators: Internet
# Time Spent: 2:00 hrs
s: str = 'HelloWorld!!'
t: str = 'ThisIsPython'
s = s.lower()
t = t.upper()
s = s.replace('a','x')
s = s.replace('r','x')
s = s.replace('l','x')
t = t.replace('P','Z')
t = t.replace('W','Z')
t = t.replace('N','Z')
fs = s[0]
ft = t[0]
ss = s.replace(fs,ft)
st = t.replace(ft,fs)
ls = len(ss)//3
lt = len(st)//3
hs = ss[ls:(ls*-1)]
ht = st[lt*-1:]
swst = ss.replace(hs,ht)
z = swst+st
print(z)