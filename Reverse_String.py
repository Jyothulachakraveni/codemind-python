n=list(map(str,input().split()))
s=[]
i=1
k=len(n)
while k!=0:
    s.append(n[-i])
    i=i+1
    k=k-1
for i in s:
    print(i,end=" ")