def fun(n):
    for i in range(len(n)):
        if n.count(n[i])==1:
            return i
    return "-1"
n=input()
print(fun(n))