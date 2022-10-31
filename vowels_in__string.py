n=input()
s="aeiou"
d="AEIOU"
f=[]
g=[]
for i in range(len(n)):
    if n[i] in s:
        if n[i] not in g:
            print(n[i],end=" ")
            g.append(n[i])
    if n[i] in d:
        if n[i] not in g:
            print(n[i],end=" ")
            g.append(n[i])
if f==g:
    print("-1")
    