def isprime(i):
    for j in range(2,i):
        if i%j==0:
            return False
    return True
n=int(input())
m=int(input())
for i in range(n,m):
    if isprime(i) and i!=1:
        print(i)