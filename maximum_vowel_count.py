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
if " " not in n:
    d.append(c)
print(max(d))