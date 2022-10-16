n=int(input())
for i in range(n):
    m=int(input())
    k=list(map(int,input().split()))
    d=(m*(m+1))//2
    print(d-sum(k))