n=int(input())
k=int(input())
for i in range(k):
    a,b=map(int,input().split())
    if n>a or n>b:
        print("UPLOAD ANOTHER")
    elif a==b:
        print("ACCEPTED")
    else:
        print("CROP IT")
        