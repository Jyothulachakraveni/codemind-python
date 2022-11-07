n=int(input())
c=0
while 2**c<=n:
    k=2**c
    c=c+1
g=2**c
if abs(n-g)>abs(n-k):
    print(abs(n-k))
else:
    print(abs(n-g))