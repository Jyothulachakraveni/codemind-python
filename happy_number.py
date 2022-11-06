n=int(input())
summ=0
while n>9:
    while n:
        d=n%10
        n=n//10
        summ=summ+d**2
    if summ>9:
        n=summ
        summ=0
    else:
        if summ==1 or summ==7:
            print("True")
        else:
            print("False")