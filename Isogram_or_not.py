def fun(n):
    for i in range(len(n)):
        if n.count(n[i])!=1:
            return False
    return True
n=input()
print(fun(n))