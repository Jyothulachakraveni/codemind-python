def fun(k):
    for i in range(len(k)):
        if k.count(k[i])!=1:
            return False
    return True
n=int(input())
k=list(str(n))
if fun(k):
    print("Unique Number")
else:
    print("Not Unique Number")