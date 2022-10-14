n=int(input())
k=n*n
summ=0
while k:
    d=k%10
    k=k//10
    summ=summ+d
if summ==n:
    print("Neon Number")
else:
    print("Not Neon Number")