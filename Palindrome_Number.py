def fun(m):
    rev=0
    while m:
        d=m%10
        m=m//10
        rev=rev*10+d
    return rev
n=int(input())
for i in range(n):
    m=int(input())
    res=fun(m)
    if res==m:
        print("True")
    else:
        print("False")