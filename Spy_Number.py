n=int(input())
p=1
summ=0
while n:
    d=n%10
    n=n//10
    summ=summ+d
    p=p*d
if summ==p:
    print("Spy Number")
else:
    print("Not Spy Number")