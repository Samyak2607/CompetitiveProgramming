for _ in range(int(input())):
    l=list(map(int,input().split()))
    x=[]
    count=0
    for i in l:
        if i!=0:
            x.append(i)
        else:
            count+=1
    for i in range(count):
        x.insert(0,0)
    print(x)
        
