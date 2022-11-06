def fun(n):
    n=str(n)
    k=n[::-1]
    if n==k:
        return k
    else:
        n=int(n)
        return fun(n+1)
def gun(n):
    n=str(n)
    k=n[::-1]
    if n==k:
        return k
    else:
        n=int(n)
        return gun(n-1)
n=int(input())
g=fun(n+1)
h=gun(n-1)
g=int(g)
h=int(h)
if abs(n-g)>abs(n-h):
    print(h)
elif abs(n-g)==abs(n-h):
    print(h,g)
else:
    print(g)