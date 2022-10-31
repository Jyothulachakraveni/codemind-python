n=int(input())
s=[]
summ=0
for i in range(n):
    m=int(input())
    s.append(m)
k=int(input())
for i in range(n):
    if s[i]<=k:
        summ=summ+1
    if s[i]>k:
        summ=summ+2
print(summ)