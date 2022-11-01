n=int(input())
for i in range(n):
    d=int(input())
    s=input()
    f=[]
    for i in range(d):
        if s.count(s[i])==1:
            f.append(s[i])
    if len(f)==0:
        print("-1")
    else:
        print(f[0])