n=input()
s=[]
c=0
for i in range(len(n)):
    if n[i]!=' ':
        c=c+1
    else:
        s.append(c)
        c=0
s.append(c)
for i in range(len(s)):
    print(s[i],end=" ")