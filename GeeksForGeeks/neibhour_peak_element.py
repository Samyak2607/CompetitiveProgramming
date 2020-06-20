for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    count=0
    
    for i in range(1,n-1):
        if (a[i]>=a[i-1]) and (a[i]>=a[i+1]):
            count+=1
    if a[0]>=a[1]:
        count+=1
    if a[n-1]>=a[n-2]:
        count+=1
    print(count)
