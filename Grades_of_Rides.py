n,m,k=map(int,input().split())
if n>50 and m>60 and k>100:
    print("10")
elif n>50 and m>60:
    print("9")
elif m>60 and k>100:
    print("8")
elif n>50 and k>100:
    print("7")
elif n>50 or m>60 or k>100:
    print("6")
else:
    print("5")