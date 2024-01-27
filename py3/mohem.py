q = int(input())
e = []
l = 0
f = []
for i in range(0,q):
    e.append(input())
for i in list(set(e)):
    r = list(i)
    for j1, j in enumerate(r):
          if j !='@':
            l += 1
          elif j == '@':
              l += 1
              break
    for k in range(l):
        r.pop(0)
    ae = ''
    for kj in r:
        ae += kj
    f.append(ae)   
    l = 0
    ae = ''
for i in sorted(list(set(f))):
    print(i)
