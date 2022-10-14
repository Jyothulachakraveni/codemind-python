def fact(n):
    q=1
    for i in range(1,n+1):
        q=q*i
    return q
def fun(n):
    summ=0
    while n:
        d=n%10
        n=n//10
        summ=summ+fact(d)
    return summ
n=int(input())
m=n
res=fun(n)
if res==m:
    print("The number "+str(m)+" is a strong number")
else:
    print("The number "+ str(m)+" is not a strong number")