n=input()
m=input()
s=[]
n=n.lower()
m=m.lower()
for i in range(len(n)):
    if n[i] not in m and n[i]!=" ":
        if n[i] not in s:
            s.append(n[i])
for i in range(len(m)):
    if m[i] not in n and m[i]!=" ":
        if m[i] not in s:
            s.append(m[i])
print(len(s))
