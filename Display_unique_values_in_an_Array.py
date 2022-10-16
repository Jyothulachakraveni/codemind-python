def fun(k):
    d=[]
    f=[]
    for i in range(n):
        if k.count(k[i])==1:
            d.append(k[i])
    if d==f:
        return "-1"
    else:
        return d
n=int(input())
k=list(map(int,input().split()))
res=fun(k)
if res=="-1":
    print("-1")
else:
    for i in range(len(res)):
        print(res[i],end=" ")
