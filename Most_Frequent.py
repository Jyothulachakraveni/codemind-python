n=int(input())
k=list(map(int,input().split()))
s=[]
g=[]
for i in range(n):
    s.append(k.count(k[i]))
f=max(s)
for i in range(n):
    if k.count(k[i])==f:
        g.append(k[i])
print(min(g))