for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    temp=10**9

    for i in range(n):
        for j in range(i+1,n):
            x=abs(a[i]-a[j])
            if x<temp:
                temp=x
    print(temp)
