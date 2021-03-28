for _ in range(int(input())):
    n,e,h,a,b,c=map(int,input().split())
    if min(e,h)<n:
        print(-1)
        continue
    if min(e,h)==n:
        print(n*c)
        continue
    if a>b and b>c:
        print(n*c)
        continue
    while(True):
        
        
        
