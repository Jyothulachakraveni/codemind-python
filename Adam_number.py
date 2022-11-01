n=int(input())
g=n*n
n=str(n)
n=n[::-1]
n=int(n)
f=n*n
f=str(f)
f=f[::-1]
f=int(f)
if f==g:
    print("True")
else:
    print("False")