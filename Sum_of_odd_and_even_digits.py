n=int(input())
k=list(map(int,input().split()))
d=0
f=0
for i in range(n):
    if i%2==0:
        d=d+k[i]
    else:
        f=f+k[i]
if (d-f==0):
    print("YES")
else:
    print("NO")