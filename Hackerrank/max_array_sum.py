for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
##    l=[]
##    x,y=0,0
##    temp=0
##    for i in range(n):
##        for j in range(i+2,n):
##            temp=max(temp,(a[i]+a[j]))
##    for i in range(n):
##        if i%2==0:
##            x+=a[i]
##        else:
##            y+=a[i]
##    x=max(x,y)
##    temp=max(temp,x)
##    print(temp)
    l=a
    l.sort(reverse=True)

    
    
    
