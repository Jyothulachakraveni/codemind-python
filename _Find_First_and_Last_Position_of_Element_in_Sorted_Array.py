n=int(input())
k=list(map(int,input().split()))
m=int(input())
s=[]
h=[]
c=0
for i in range(n):
    if k[i]==m:
        s.append(c)
    c+=1
if s==h:
    print("-1 -1")
else:
    print(s[0],s[-1])