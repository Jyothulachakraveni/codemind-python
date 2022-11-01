n=list(map(str,input().split()))
s=[]
for i in range(len(n)):
    if i%2==0:
        k=n[i]
        s.append(k[::-1])
    else:
        s.append(n[i])
for i in s:
    print(i,end=" ")