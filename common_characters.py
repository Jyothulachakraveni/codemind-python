n=input()
m=input()
s=[]
n=n.lower()
m=m.lower()
for i in range(len(n)):
    if n[i] in m and n[i]!=" ":
        if n[i] not in s:
            s.append(n[i])
s.sort()
if len(s)==0:
    print("-1")
else:
    for i in s:
        print(i,end="")