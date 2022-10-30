def fun(d):
    s=0
    while d:
        f=d%10
        d=d//10
        s=s+1
    if s%2==0:
        return True
    else:
        return False
n=int(input())
k=list(map(int,input().split()))
c=0
for i in range(n):
    if fun(k[i]):
        c=c+1
print(c)