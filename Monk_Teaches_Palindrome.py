n=int(input())
for i in range(n):
    s=input()
    r=s[::-1]
    if s==r:
        if len(s)%2==0:
            print("YES EVEN")
        else:
            print("YES ODD")
    else:
        print("NO")