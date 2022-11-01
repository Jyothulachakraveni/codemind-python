n=input()
c=0
s="aeiou"
n.lower()
d=[]
for i in range(len(n)):
    if n[i] in s:
        c=c+1
    if n[i]==" ":
        d.append(c)
        c=0
    if n.count(" ")!=0:
        if len(n)-1==i:
            d.append(c)
if " " not in n:
    d.append(c)
x=max(d)
print(d.count(x))