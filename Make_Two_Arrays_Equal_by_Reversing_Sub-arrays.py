def fun(n,k,d):
    for i in range(n):
        if k[i] not in d:
            return False
    for i in range(n):
        if d[i] not in k:
            return False
    return True
n=int(input())
k=list(map(int,input().split()))
m=int(input())
d=list(map(int,input().split()))
if fun(n,k,d):
    print("True")
else:
    print("False")