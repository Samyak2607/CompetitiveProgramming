for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    if len(set(a))<m:
        print('Yes')
    else:
        print('No')
