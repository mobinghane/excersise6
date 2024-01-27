q = list(bin(int(input()))[2::])
w = list(bin(int(input()))[2::])
e = int(input())
del q[0]
del q[1]
del w[0]
del w[1]
while len(q)<32:
     q.insert(0,'0')
while len(w)<32:
     w.insert(0,'0')
r = w + q
t = []
for i in range (1, e+1):
     t.append(input())
for i in t:
     if r[63-int(i)] == '0':
         print('no')
     else:
         print('yes')     



