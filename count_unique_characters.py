n=input()
n=n.lower()
c=0
for i in range(len(n)):
    if n[i]!=" ":
        if n.count(n[i])==1:
            c=c+1
print(c)