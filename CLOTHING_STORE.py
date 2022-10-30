n=int(input())
k=list(map(int,input().split()))
g=set(k)
h=list(g)
s=[]
c=0
for i in range(len(h)):
    s.append(k.count(h[i]))
for i in range(len(s)):
    d=s[i]//2
    c=c+d
print(c)