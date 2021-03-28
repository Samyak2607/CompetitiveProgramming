r,o,c=map(int,input().split())
if c>r:
    print('Yes')
else:
    o=20-o
    if 36*o+c>r:
        print('Yes')
    else:
        print('No')

    
