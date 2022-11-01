a,b=map(str,input().split())
c=int(b)
k=a[0:c]
g=a[-c:]
k=int(k)
g=int(g)
print(abs(k-g))