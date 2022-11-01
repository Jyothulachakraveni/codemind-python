n=int(input())
k=list(map(str,input().split()))
s=[]
c=0
for i in range(n):
    d=k[i]
    s.append(len(d))
f=min(s)
for i in range(n):
    d=k[i]
    if len(d)==f:
        c=c+1
print(c)