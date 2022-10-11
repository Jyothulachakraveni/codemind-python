n=int(input())
k=list(map(int,input().split()))
for i in range(n):
    d=k[i]
    if k.count(d)==1:
        print(d)