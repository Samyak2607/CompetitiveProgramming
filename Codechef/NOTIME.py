n,h,x=map(int,input().split())
t=list(map(int,input().split()))
if h<=x:
    print("YES")
else:
    req=h-x
    if req in t:
        print("YES")
    else:
        
        print("NO")
