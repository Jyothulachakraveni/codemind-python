n=int(input())
num=n*n
def fun(n,num):
    while n:
        if num%10!=n%10:
            return False
        n=n//10
        num=num//10
    return True
if fun(n,num):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")