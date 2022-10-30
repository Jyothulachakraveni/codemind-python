n=int(input())
k=list(map(int,input().split()))
s=[]
for i in range(n):
    g=k.count(k[i])
    s.append(g)
f=max(s)
for i in range(n):
    if f==k.count(k[i]):
        print(k[i])
        break