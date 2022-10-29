def fun(i):
    d=str(i)
    g=d[::-1]
    if g==d:
        return True
    else:
        return False
n=input()
k=n.lower()
k=k.split()
c=0
for i in range(len(k)):
    if fun(k[i]):
        c=c+1
print(c)