for _ in range(int(input())):
    h,p=map(int,input().split())
    while(p>0):
        h=h-p
        if h<=0:
            break
        p=p//2

    if h>0:
        print(0)
    else:
        print(1)
