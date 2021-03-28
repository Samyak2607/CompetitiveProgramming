for _ in range(int(input())):
    w1,w2,x1,x2,m=map(int,input().split())
    w1=w2-w1
    x=m*(min(x1,x2))
    y=m*(max(x1,x2))

    
    if w1>=x and w1<=y:
        print(1)
    else:
        print(0)
    
        
    
