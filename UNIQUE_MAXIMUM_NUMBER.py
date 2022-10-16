n=int(input())
k=list(map(int,input().split()))
d=[]
f=[]
for i in range(n):
    if k.count(k[i])==1:
        d.append(k[i])
if d==f:
    print("-1")
else:
    print(max(d))