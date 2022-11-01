s=input()
n=len(s)
c=0
d=0
ans=0
for i in range(n):
    if s[i]=='R':
        c=c+1
    if s[i]=='L':
        d=d+1
    if c==d:
        ans=ans+1
print(ans)