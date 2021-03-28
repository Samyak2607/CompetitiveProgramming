for _ in range(int(input())):
    n,k=map(int,input().split())
    if n==k:
        print(1,n)
    else:
        if n%k==0:
            print(n//k,k)
        else:
            print((n//k)+1,n%k)
