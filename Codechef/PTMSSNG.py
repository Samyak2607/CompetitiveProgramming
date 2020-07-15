for _ in range(int(input())):
    n=int(input())
    N=4*n
    """
    l=[]
    X=[]
    Y=[]
    
    for i in range(N-1):
        x,y=map(int,input().split())
        temp=(x,y)
        X.append(x)
        Y.append(y)
    temp_x=X.count(1)
    temp_y=Y.count(1)
    for i in range(2,(N//2)+1):
        temp=X.count(i)
        if temp!=temp_x:
            if temp>temp_x:
                x=i-1
            else:
                x=i
            flag=1
        else:
            flag=0
            temp_x=temp
            
        temp=Y.count(i)

        if temp!=temp_y:
            if temp>temp_y:
                y=i-1
            else:
                y=i
            flag=1
        else:
            flag=0
            temp_y=temp
        if flag:
            break
    print(x,y)
    """
    l=[]
    for i in range(N-1):
        x,y=map(int,input().split())
        temp=(x,y)
        l.append(temp)
    for i in l:
        x=i[0]
        y=i[1]
        temp1=(x+1,y)
        temp2=(x,y+1)
        temp3=(x+1,y+1)
        if temp1 not in l:
            print(temp1)
            break
        if temp2 not in l:
            print(temp2)
            break
        if temp3 not in l:
            print(temp3)
            break

        
    
    
