def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
n=int(input())
s=[]
for i in range(1,n+1):
    if n%i==0:
        if isprime(i)==False:
            s.append(i)
print(len(s)+1)