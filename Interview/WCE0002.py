for _ in range(int(input())):
    d,k=map(int,input().split())
    if d==k:
        print('YES')
    elif d<k and d<(k-1):
        print("NO")
    else:
        if d%k==0 or d%(k-1)==0:
            print("YES")
        else:
            rem=d%k
            pr=d//k
            req=k-rem
            if req<=pr:
                print("YES")
            else:
                print("NO")
            
    
