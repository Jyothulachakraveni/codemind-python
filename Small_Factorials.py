def fun(m):
    p=1
    for i in range(1,m+1):
        p=p*i
    return p
n=int(input())
for i in range(n):
    m=int(input())
    res=fun(m)
    print(res)