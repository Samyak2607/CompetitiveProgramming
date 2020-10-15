for _ in range(int(input())):
    n,x,p,k=map(int,input().split())
    l=list(map(int,input().split()))
    flag,ans=0,0
    l.sort()
    if x not in l:
        print(-1)
    else:
        ind=l.index(x)
        if (p-1)>ind:
            ans=p-1-ind
        elif (p-1)==ind:
            ans=0
        else:
            ans=ind-(p-1)
        print(ans)
            
                
    
