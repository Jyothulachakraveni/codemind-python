n=input()
s=[]
for i in range(len(n)):
    if n[i]==".":
        s.append("[.]")
    else:
        s.append(n[i])
for i in s:
    print(i,end="")