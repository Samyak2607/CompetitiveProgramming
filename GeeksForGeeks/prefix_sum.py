for _ in range(int(input())):
    a=list(map(int,input().split()))
    n=len(a)
    ps=0
    
    for i in range(n):
        a[i]+=ps
        ps=a[i]
    print(a)
