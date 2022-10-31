n=input()
n=n.lower()
c=1
s=[]
d=[]
for i in range(len(n)):
    if n.count(n[i])==1:
        print(n[i])
        s.append(c)
        break
if s==d:
    print("-1")