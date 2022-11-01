n=list(map(str,input().split()))
m=list(map(str,input().split()))
s=[]
for i in range(len(m)):
    if str(m[i]).lower() in n and m[i]!=" ":
        if m[i] not in s:
            s.append(str(m[i]).lower())
for i in range(len(n)):
    if str(n[i]).lower() in m and n[i]!=" ":
        if n[i] not in s:
            s.append(str(n[i]).lower())
for i in s:
    print(i,end=" ")