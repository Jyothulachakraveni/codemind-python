n=int(input())
k=list(map(int,input().split()))
s=[]
for i in range(1,n+1):
    if i not in k:
        s.append(i)
print(min(s))