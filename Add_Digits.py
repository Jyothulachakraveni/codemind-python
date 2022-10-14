def fun(n):
    summ=0
    while n:
        d=n%10
        n=n//10
        summ=summ+d
    if summ>9:
        return fun(summ)
    else:
        return summ
n=int(input())
res=fun(n)
print(res)
    