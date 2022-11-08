def fun(k):
    k=str(k)
    s=[]
    for i in k:
        s.append(ord(i))
    d=min(s)
    for i in k:
        if ord(i)==d:
            return i
def gun(k):
    k=str(k)
    s=[]
    for i in k:
        s.append(ord(i))
    d=max(s)
    for i in k:
        if ord(i)==d:
            return i
n=list(map(str,input().split()))
summ=0
summ2=0
for i in range(len(n)):
    k=n[-1]
    d=n[0]
    res=fun(d)
    res2=gun(k)
print(res,res2)