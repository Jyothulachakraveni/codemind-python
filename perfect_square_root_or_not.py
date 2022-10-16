def fun(n):
    for i in range(1,n):
        if i*i==n:
            return True
    return False
n=int(input())
print(fun(n))