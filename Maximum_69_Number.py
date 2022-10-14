n=int(input())
c=0
rev=0
while n:
    d=n%10
    n=n//10
    rev=rev*10+d
while rev:
    k=rev%10
    rev=rev//10
    if k==6:
        if c==0:
            k=9
            c=c+1
    print(k,end="")