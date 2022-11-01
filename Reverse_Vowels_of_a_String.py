n=input()
s="AEIOUaeiou"
d=[]
a=[]
for i in range(len(n)):
    if n[i] in s:
        d.append(n[i])
f=d[::-1]
u=0
for i in range(len(n)):
    if n[i] in s:
        a.append(f[u])
        u=u+1
    else:
        a.append(n[i])
for i in a:
    print(i,end="")