for _ in range(int(input())):
    n,k,x,y=map(int,input().split())
    flag=0
    for i in range(n):
        if x==y:
            flag=1
            break
        x=(x+k)%n

    if flag:
        print('YES')
    else:
        print('NO')
    
