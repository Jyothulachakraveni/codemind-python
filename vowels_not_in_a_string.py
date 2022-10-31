def fun(n,s):
    d=[]
    f=[]
    for i in s:
        if i not in n:
            d.append(i)
        
    if d==f:
        return "0"
    else:
        return d
n=input()
s="aeiou"
res=fun(n,s)
if res==0:
    print(res)
else:
    for i in range(len(res)):
        print(res[i],end=" ")