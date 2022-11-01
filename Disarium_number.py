n=input()
s=len(n)
n=int(n)
summ=0
g=n
while n:
    d=n%10
    n=n//10
    summ=summ+d**s
    s=s-1
if summ==g:
    print("True")
else:
    print("False")