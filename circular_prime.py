def prime(k):
    for i in range(2,k):
        if k%i==0:
            return False
    return True
n=int(input())
n=str(n)
rev=n[::-1]
n=int(n)
rev=int(rev)
if prime(n):
    if prime(rev):
        print("circular prime")
    else:
        print("prime but not a circular prime")
else:
    print("not prime")