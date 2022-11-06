def fun(s):
    for i in range(len(s)):
        for j in range(len(s)):
            if s[i]*s[j]==n:
                return s[i],s[j]
    return "-1"
def primt(i):
    for j in range(2,i):
        if i%j==0:
            return False
    return True
n=int(input())
s=[]
for i in range(2,n):
    if primt(i):
        s.append(i)
if fun(s)=="-1":
    print("-1")
else:
    a,b=fun(s)
    print(a,b)