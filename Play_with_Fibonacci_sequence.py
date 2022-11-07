n=int(input())
a=0
b=1
n=n-2
print(a,b,end=" ")
while n:
    c=a+b
    print(c,end=" ")
    a=b
    b=c
    n=n-1