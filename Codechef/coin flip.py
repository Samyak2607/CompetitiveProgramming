for _ in range(int(input())):
    g = int(input())
    for i in range(g):
        i,n,q = map(int,input().split())
        ans = n//2
        if i==q:
            print(ans)
        else:
            print(n-ans)
        
