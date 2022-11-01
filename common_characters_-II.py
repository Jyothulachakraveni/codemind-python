n=input()
m=input()
s=[]
n=n.lower()
m=m.lower()
for i in range(len(n)):
    if n[i] in m and n[i]!=" ":
        if n[i] not in s:
            s.append(n[i])
print(len(s))