def Sorting(k):
    l = sorted(k)
    return l
k=list(map(str,input().split()))
res=Sorting(k)
for i in res:
    print(i,end=" ")