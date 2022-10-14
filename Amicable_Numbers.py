n=int(input())
m=int(input())
s=[]
d=[]
for i in range(1,n):
    if n%i==0:
        s.append(i)
for i in range(1,m):
    if m%i==0:
        d.append(i)
if sum(d)==n:
    if sum(s)==m:
        print("Amicable")
else:
    print("Not Amicable")