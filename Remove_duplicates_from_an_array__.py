n=int(input())
k=list(map(int,input().split()))
k=set(k)
k=list(k)
for i in range(len(k)):
    print(k[i],end=" ")