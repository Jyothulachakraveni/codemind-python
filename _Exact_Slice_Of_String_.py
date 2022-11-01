n=input()
a=int(input())
b=int(input())
for i in range(len(n)):
    if i>=a and i<=b:
        print(n[i],end="")