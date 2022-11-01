n=int(input())
for i in range(n):
    s=input()
    c=0
    for i in range(len(s)):
        if s[i].isdigit():
            c=c+1
    if c==0:
        print("No")
    else:
        print("Yes")