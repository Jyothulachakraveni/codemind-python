n=int(input())
k=list(map(str,input().split()))
s=[]
for i in range(n):
    d=k[i]
    s.append(len(d))
f=max(s)
for i in range(n):
    d=k[i]
    if len(d)==f:
        print(d,end=" ")