n=int(input())
k=list(map(int,input().split()))
m=int(input())
d=list(map(int,input().split()))
s=int(input())
c=0
for i in range(n):
    if s>=k[i] and d[i]>=s:
        c=c+1
print(c)