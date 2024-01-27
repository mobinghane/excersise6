def numberToBase(n, b):
    if b < 2 or b > 9:
        return 0
    else:
        if n == 0:
            return [0]
        digits = []
        while n:
            digits.append(int(n % b))
            n //= b
        digits = digits[::-1]
        kh = 0
        for k, x in enumerate(digits):
            kh += x * 10**(len(digits)-1-k)
        return kh
u = 0
res = 0
wnum1 = []
qbase1 = []
while True:
    w,q=map(int,input().split())
    wnum1.append(w)
    qbase1.append(q)
    if w == -1:
        break    
stop = True
qbase1.pop(-1)    
wnum1.pop(-1)
for i in qbase1 :
    if i>9 or i<2 :
        print ('invalid base!')
        stop = False
        break
if stop:
    for i1,i in enumerate(wnum1):
        for j in range(1,i+1):
            if i%j == 0:
                res += j
        u+=numberToBase(res,qbase1[i1])
        res=0     
    print(u)
