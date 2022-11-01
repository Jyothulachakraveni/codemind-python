n=input()
s=[]
for i in range(len(n)):
    if n[i].isdigit():
        s.append(int(n[i]))
print(sum(s))
