n=int(input())
s=[]
k=list(map(int,input().split()))
for i in range(n):
    d=k[i]*k[i]
    s.append(d)
s.sort()
for i in range(len(s)):
    print(s[i],end=" ")