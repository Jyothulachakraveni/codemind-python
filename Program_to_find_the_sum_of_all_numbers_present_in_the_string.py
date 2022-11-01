n=input()
c=0
for i in range(len(n)):
    if n[i].isdigit():
        c=c+int(n[i])
print(c)