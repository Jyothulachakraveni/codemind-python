n=list(map(str,input().split()))
d=n[-1]
s=[]
for i in range(len(d)):
    s.append(ord(d[i]))
g=min(s)
for i in range(len(d)):
    if ord(d[i])==g:
        if d[i].lower() in d:
            print(d[i].lower())
        else:
            print(d[i])