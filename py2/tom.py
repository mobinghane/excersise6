q=[]
def gcd (a,b):
    if (b == 0):
        return a
    else:
         return gcd (b, a % b)
o = ['sum','max','min','gcd','lcd','average']
f = input()
if f in o:
    while True:
        t=input()
        q.append(t)
        if t=='end':
            break   
    q.pop(-1)
    if f =='sum':
        e = [eval(i) for i in q]
        print(sum(e))
    elif f =='average':
        r = [eval(i) for i in q]
        print(round(sum(r)/len(r),2))
    elif f =='max':
        t = [eval(i) for i in q]
        print(max(t))
    elif f=='min':
        t = [eval(i) for i in q]
        print(min(t))
    elif f =='gcd':
        y = [eval(i) for i in q]
        res = y[0]
        for c in y[1::]:
            res = gcd(res , c)
        print(res) 
    elif f =='lcd':
        h = [eval(i) for i in q]
        lcm = 1
        for i in h:
            lcm = lcm * i // gcd(lcm, i)
        print(lcm)
else:
    print('Invalid command')
        
    




