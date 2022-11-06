def prime(n):
    for i in range(2,n):
        if n%i==0:
            return prime(n+1)
    return n
def prime2(n):
    for i in range(2,n):
        if n%i==0:
            return prime2(n-1)
    return n
m=int(input())
for i in range(m):
    n=int(input())
    k=prime(n)
    h=prime2(n)
    if abs(n-k)>abs(n-h):
        print(h)
    elif abs(n-k)==abs(n-h):
        print(min(k,h))
    else:
        print(k)