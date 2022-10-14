def fun(n):
    for i in range(n):
        if i*i==n:
            return True
    return False
m=int(input())
for i in range(m):
    n=int(input())
    res=fun(n)
    print(res)