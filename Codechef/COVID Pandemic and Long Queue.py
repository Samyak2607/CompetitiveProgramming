t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    l=[]
    flag=0
    for i in range(n):
        if l:
            if a[i]==1:
                temp = i-l[-1]
                if temp < 6:
                    flag=1
                    break
                else:
                    l.append(i)
                    
        else:
            if a[i]==1:
                l.append(i)
    if flag==0:
        print('YES')
    else:
        print('NO')
            
