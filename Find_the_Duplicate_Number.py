n=int(input())
k=list(map(int,input().split()))
for i in range(n):
    if k.count(k[i])!=1:
        print(k[i])
        break