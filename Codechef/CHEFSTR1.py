for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    count=0

    for i in range(1,n):
        if a[i]==a[i-1]:
            continue
        count+=(abs(a[i]-a[i-1])-1)
    print(count)
