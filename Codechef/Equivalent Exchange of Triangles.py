t = int(input())
for _ in range(t):
    n = int(input())
    color = list(map(int,input().split()))
    col = {}
    for c in color:
        if c in col:
            col[c]+=1
        else:
            col[c]=1
    print(col)
    
