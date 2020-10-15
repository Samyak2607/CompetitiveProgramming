for _ in range(int(input())):
    n,k=map(int,input().split())
    q=list(map(int,input().split()))
    count=0
    rem=0
    flag=0
    for i in range(n):
        if q[i]<k:
            if (q[i]+rem)<k:
                count+=1
                flag=1
                break
            else:
                count+=1
                rem-=(k-q[i])
        
        count+=1
        rem+=(q[i]-k)
    if flag:
        print(count)
    elif rem:
        count+=(rem//k)+1
        print(count)
        
        
        
