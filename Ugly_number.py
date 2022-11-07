def fun(n):
    if n<0:
        return False
    fact=[2,3,5]
    for i in fact:
        while n%i==0:
            n/=i
    return n==1
n=int(input())
if fun(n):
    print("Ugly Number")
else:
    print("Not Ugly Number")