for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    x,i,swap,flag=0,0,0,0

    l=list(a)

##    while(i!=(n-1)):
##        if a[i]>a[i+1]:
##            print('before')
##            print(a[i],a[i+1])
##            temp=a[i]
##            a[i]=a[i+1]
##            a[i+1]=temp
##            print('After')
##            print(a[i],a[i+1])
##            swap+=1
##        i+=1
##    print(l)
##    print(a)
##    for i in l:
##        indl=l.index(i)
##        inda=a.index(i)
##        if abs(inda-indl)>2:
##            flag=1
##            break
    l=list(a)
    l.sort()
    for i in l:
        indl=l.index(i)
        inda=a.index(i)
        if (indl-inda)>2:
            flag=1
            break
    for i in range(n):
        for j in range(i+1,n):
            if a[i]>a[j]:
                temp=a[i]
                a[i]=a[j]
                a[j]=temp
                swap+=1
        
    if flag:
        print('Too chaotic')
    else:
        print(swap)













        
