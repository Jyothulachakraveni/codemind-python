n=int(input())
k=list(map(int,input().split()))
k=set(k)
k=list(k)
k.sort()
if n>=3:
    print(k[-3])
else:
    if n==2:
        print(k[-1])
    if n==1:
        print(k[0])