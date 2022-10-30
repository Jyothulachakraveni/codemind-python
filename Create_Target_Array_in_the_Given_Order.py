n=int(input())
k=list(map(int,input().split()))
m=int(input())
d=list(map(int,input().split()))
s=[]
for i in range(n):
    s.insert(d[i],k[i])
for i in range(len(s)):
    print(s[i],end=" ")