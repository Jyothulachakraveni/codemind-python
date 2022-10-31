a,b=map(int,input().split())
k=list(map(int,input().split()))
s=[]
c=0
for i in range(a):
    d=k[i]
    if d<0:
        d=-(d)
    d=str(d)
    if len(d)==b:
        c=c+1
print(c)