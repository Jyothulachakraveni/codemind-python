def gcd(a,b):
    while b:
        a,b=b,a%b
    return abs(a)
a,b=map(int,input().split())
print(gcd(a,b))