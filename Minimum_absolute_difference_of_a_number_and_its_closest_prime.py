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
n=int(input())
k=prime(n)
h=prime2(n)
if abs(n-k)>abs(n-h):
    print(abs(n-h))
else:
    print(abs(n-k))