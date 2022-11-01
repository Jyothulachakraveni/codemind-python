n=input()
s=input()
c=0
for i in range(len(n)):
    if n[i]==s[0]:
        c=c+1
if c==0:
    print("-1")
else:
    print(c)