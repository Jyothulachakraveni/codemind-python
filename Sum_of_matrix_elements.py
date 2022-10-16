n=int(input())
m=int(input())
summ=0
for i in range(n):
    k=list(map(int,input().split()))
    for i in range(m):
        summ=summ+k[i]
print(summ)