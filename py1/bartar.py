q,w=map(int,input().split())
if q>w:
  x=range(q,w+1)
else:
  x=range(w,q+1)
e =[]
for i in x:
  e.append(i)
  for j in range(2,i):
    if i%j==0:
     e.remove(i)
     break
for k in e:
  if k == 0:
    e.remove(k)
for k in e:
  if k == 1:
    e.remove(k)
if w>=q:
  print("main order - amount:",len(e))
else:
  print("reverse order - amount:",len(e))