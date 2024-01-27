x=int(input())
y=int(input())
r=int(input())
d=x,y
q=list(d)
s=sum(q)
print(s)
if r==s:
    print('YES')
else:
    print('NO')