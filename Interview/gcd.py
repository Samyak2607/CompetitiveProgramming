for _ in range(int(input())):
    a,b=map(int,input().split())
    end=max(a,b)
    f=1
    for i in range(end,1,-1):
        if a%i==0 and b%i==0:
            f=1
            break
    if f:
        print(i)
    else:
        print(1)
        
        
