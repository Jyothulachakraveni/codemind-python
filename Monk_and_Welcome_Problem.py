n=int(input())
k=list(map(int,input().split()))
d=list(map(int,input().split()))
s=[]
for i in range(n):
    s.append(k[i]+d[i])
for i in range(len(s)):
    print(s[i],end=" ")