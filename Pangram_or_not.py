def fun(n):
    for i in range(97,123):
        if chr(i) not in n:
            return False
    return True
n=input()
n=n.lower()
print(fun(n))