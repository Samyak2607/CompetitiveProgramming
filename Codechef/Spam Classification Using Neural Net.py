t = int(input())
for _ in range(t):
    b_list=0
    even=0
    odd=0
    temp=1
    n,minx,maxx = map(int,input().split())
    for i in range(n):
        w,b = map(int,input().split())
        b_list+=b
        if i==0:
            temp1=w
            continue
        else:
            temp*=(1+w)
    for i in range(minx, maxx+1):
        x = temp*temp1*i+b_list
        if x%2 == 0:
            even+=1
        else:
            odd+=1
    print(even, odd)
