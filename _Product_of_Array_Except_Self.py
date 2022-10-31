n=int(input())
k=list(map(int,input().split()))
p=1
s=[]
for i in range(n):
    g=k[i]
    for i in range(n):
        if k[i]!=g:
            p=p*k[i]
    s.append(p)
    p=1
for i in range(len(s)):
    print(s[i],end=" ")
        