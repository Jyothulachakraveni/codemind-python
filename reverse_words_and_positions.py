n=list(map(str,input().split()))
s=[]
for i in range(len(n)):
    k=n[i]
    s.append(k[::-1])
s.reverse()
for i in s:
    print(i,end=" ")