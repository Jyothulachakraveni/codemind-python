def fun(n):
    for i in range(n):
        if i*(i+1)==n:
            return True
    return False
n=int(input())
if fun(n):
    print("YES")
else:
    print("NO")
        