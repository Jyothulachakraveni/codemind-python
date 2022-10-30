n=int(input())
k=list(map(int,input().split()))
d=k.count(0)
s=[]
for i in range(n):
    if k[i]!=0:
        s.append(k[i])
for i in range(d):
    s.append(0)
for i in range(len(s)):
    print(s[i],end=" ")