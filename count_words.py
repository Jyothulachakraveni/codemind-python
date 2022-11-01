n=list(map(str,input().split()))
s="aeiou"
g="AEIOU"
c=0
for i in range(len(n)):
    d=n[i]
    if d[0] in s or d[0] in g:
        if d[-1] not in s and d[-1] not in g:
            c=c+1
print(c)