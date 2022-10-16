def fun(f,k):
    c=0
    for i in range(len(k)):
        if k[i]<f:
            c=c+1
    return c
n=int(input())
k=list(map(int,input().split()))
for i in range(n):
    res=fun(k[i],k)
    print(res,end=" ")