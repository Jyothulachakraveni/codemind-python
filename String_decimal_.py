n=int(input())
for i in range(n):
    s=input()
    c=0
    for i in range(len(s)):
        if s[i].isdigit():
            c=c+1
    if c==len(s):
        print("True")
    else:
        print("False")