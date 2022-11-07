def prime(n):
    for i in range(2,n):
        if n%i==0:
            return False
    return True
def fun(n):
    while n:
        d=n%10
        n=n//10
        if prime(d) and d!=1 and d!=0:
            continue
        else:
            return False
    return True
n=int(input())
if prime(n) and n!=1:
    if fun(n):
        print("Mega Prime")
    else:
        print("Not Mega Prime")
else:
    print("Not Mega Prime")