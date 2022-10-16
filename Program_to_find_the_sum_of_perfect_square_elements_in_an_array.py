def fun(k):
    for i in range(1,k+1):
        if i*i==k:
            return True
    return False
n=int(input())
d=list(map(int,input().split()))
summ=0
for i in range(n):
    if fun(d[i]):
        summ=summ+d[i]
print(summ)