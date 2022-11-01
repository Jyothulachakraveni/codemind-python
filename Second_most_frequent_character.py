n=input()
s=[]
c=0
f=set(n)
g=list(f)
for i in range(len(g)):
    s.append(n.count(g[i]))
s.sort()
s=set(s)
s=list(s)
if len(s)==1:
    print("-1")
else:
    for i in range(len(n)):
        if n.count(n[i])==s[-2]:
            print(n[i])
            break