n=input()
n.lower()
c=0
for i in range(len(n)):
    if (n[i].isalpha()):
        continue
    elif (n[i].isdigit()):
        continue
    elif n[i]==" ":
        continue
    else:
        c=c+1
print(c)