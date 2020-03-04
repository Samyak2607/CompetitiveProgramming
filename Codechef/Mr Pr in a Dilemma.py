t = int(input())
for _ in range(t):
    a,b,c,d = map(int,input().split())
    if c == d:
        if a==b:
            print('YES')
        else:
            print('NO')
    else:
        if (a-b)%(c-d) == 0:
            print('YES')
        else:
            print('NO')

            
            
            
