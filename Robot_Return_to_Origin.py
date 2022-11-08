def fun(n):
    if n.count('L')!=n.count('R'):
        return False
    if n.count('U')!=n.count('D'):
        return False
    return True
n=input()
print(fun(n))