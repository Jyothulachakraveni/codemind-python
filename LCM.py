def fun(a,b):
    if a>b:
        greater=a
    else:
        greater=b
    while True:
        if greater%a==0 and greater%b==0:
            lcm=greater
            break
        greater+=1
    return lcm
a,b=map(int,input().split())
print(fun(a,b))