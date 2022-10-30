n=int(input())
k=list(map(int,input().split()))
d=int(input())
s=[]
r=max(k)
for i in range(n):
    if (r-k[i])<=d:
        s.append(True)
    else:
        s.append(False)
for i in range(n):
    print(s[i],end=" ")
        