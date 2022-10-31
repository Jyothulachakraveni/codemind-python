n=int(input())
k=list(map(int,input().split()))
s=n//2
d=k[s:]
d.reverse()
for i in range(s):
    d.append(k[i])
for i in range(len(d)):
    print(d[i],end=" ")