n=int(input())
k=list(map(int,input().split()))
s=[]
for i in range(n):
    d=k[i]
    if d<0:
        d=-(d)
    d=str(d)
    s.append(len(d))
for i in range(len(s)):
    print(s[i],end=" ")