for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    l=[a[0],a[n-1],0]
    ind=[0,n-1]
    m=abs(a[0]-a[len(a)-1])
    for i in range(1,len(a)-1):
        if m<(a[n-1-i]-a[i]):
            m=a[n-1-i]-a[i]
            l=[a[i],a[n-1-i],0]
            ind=[i,n-1-i]
            
    m=-10**9

    for i in range(n):
        if i not in ind:
            if abs(l[0]-a[i])>m or abs(l[1]-a[i])>m:
                l[2]=a[i]
                m=max(abs(l[0]-i), abs(l[1]-i))
    ans=abs(l[0]-l[1])+abs(l[1]-l[2])+abs(l[2]-l[0])
    print(ans)
    
    
