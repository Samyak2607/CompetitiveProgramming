for _ in range(int(input())):
    n,m=map(int,input().split())
    f=list(map(int,input().split()))
    c=list(map(int,input().split()))

    i,j,count=0,0,0
    t=0
        
    while(True):
        try:
            if f[i]>c[j]:
                c[j]=t+1
                j+=1
                
            else:
                f[i]=t+1
                i+=1
            t+=1
        except IndexError:
            break
    if len(f)>len(c):
        for k in range(i+1,len(f)):
            f[k]=t+1
            t+=1
    else:
        for k in range(j+1,len(c)):
            c[k]=t+1
            t+=1
    
        
            
