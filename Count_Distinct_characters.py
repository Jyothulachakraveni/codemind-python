n=input()
n=n.lower()
s=[]
for i in range(len(n)):
    if n[i]!=' ':
        if n[i] not in s:
            s.append(n[i])
s.sort()
print(len(s))