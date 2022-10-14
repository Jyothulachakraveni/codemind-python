n=int(input())
summ=0
p=1
while n:
    d=n%10
    n=n//10
    p=p*d
    summ=summ+d
print(p-summ)