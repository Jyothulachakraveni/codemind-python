def fun(n,s):
    for i in range(len(s)):
        if s[i] in n:
            continue
        else:
            return False
    return True
n=input()
n.lower()
s="aeiou"
print(fun(n,s))