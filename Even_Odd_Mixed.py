n=input()
d=list(n)
c=0
k=0
for i in range(len(d)):
    if int(d[i])%2==0:
        c=c+1
    else:
        k=k+1
if c==len(d):
    print("Even")
elif k==len(d):
    print("Odd")
else:
    print("Mixed")
    