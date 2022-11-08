def fun(k):
    k=str(k)
    s=[]
    for i in k:
        s.append(ord(i))
    return min(s)
def gun(k):
    k=str(k)
    s=[]
    for i in k:
        s.append(ord(i))
    return max(s)
n=list(map(str,input().split()))
summ=0
summ2=0
for i in range(len(n)):
    k=n[i]
    res=fun(k)
    summ=summ+res
    res2=gun(k)
    summ2=summ2+res2
print(abs(summ2-summ))