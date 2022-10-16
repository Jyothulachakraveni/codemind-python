n=int(input())
rev=0
m=n
while n:
    d=n%10
    n=n//10
    rev=rev*10+d
if rev==m:
    print("True")
else:
    print("False")