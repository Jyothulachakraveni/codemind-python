n=input()
s=input()
d=n+s
d=list(d)
d.sort()
for i in range(len(d)):
    print(d[i],end="")