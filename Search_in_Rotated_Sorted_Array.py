n=int(input())
k=list(map(int,input().split()))
m=int(input())
if m in k:
    print(k.index(m))
else:
    print("-1")