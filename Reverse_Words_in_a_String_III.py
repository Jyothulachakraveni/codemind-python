k=list(map(str,input().split()))
s=[]
for i in range(len(k)):
    d=k[i]
    d=str(d)
    f=d[::-1]
    s.append(f)
for i in range(len(s)):
    print(s[i],end=" ")