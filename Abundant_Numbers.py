n=int(input())
summ=0
for i in range(1,n):
    if n%i==0:
        summ=summ+i
if summ>n:
    print("True")
else:
    print("False")