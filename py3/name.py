import re
z= []
x= []
#words = '!10 o4 g6 l3 l2 u7 H0 /5 y8 e1 s9'
t = re.split('\s', input())
l = 0
for i in range(len(t)):
    c = t[0]
    c1 = list(c)
    z.append(c1[0])
    c1.pop(0)
    for j1,j in enumerate(c1):
        l += int(j) * 10 ** (len(c1)-j1-1)
    x.append(l)
    l = 0
    t.pop(0)
z_copy = z.copy()
for i1, i in enumerate(z):
    z_copy[int(x[i1])] = z[i1]
for i in z_copy:
    print(i, end= '')