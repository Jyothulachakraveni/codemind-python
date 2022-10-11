import math
n,m,k=map(int,input().split())
s=(n+m+k)/2
d=math.sqrt(s*(s-n)*(s-m)*(s-k))
print('%.2f'%d)