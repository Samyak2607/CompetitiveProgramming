for _ in range(int(input())):
    n,m=map(int,input().split())
    l=list(map(int,input().split()))
    ans=sum(l)-m
    
    ans=ans//n
    end=max(l)
    for i in range(ans,end+1):
        res=0
        for j in l:
            if j>i:
                res+=(j-i)
        if res==m:
            print(i)
            break
    
