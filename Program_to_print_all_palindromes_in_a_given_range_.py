def palin(i):
    rev=0
    h=i
    while i:
        d=i%10
        i=i//10
        rev=rev*10+d
    if rev==h:
        return True
    else:
        return False
n=int(input())
m=int(input())
for i in range(n,m):
    if palin(i):
        print(i,end=" ")