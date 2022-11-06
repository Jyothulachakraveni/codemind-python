n=int(input())
m=n
n=abs(n)
rev=0
while n:
    d=n%10
    n=n//10
    rev=rev*10+d
if m>0:
    print(rev)
else:
    print(-(rev))