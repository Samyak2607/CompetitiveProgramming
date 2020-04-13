t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int,input().split()))
    sum=0
    i=0
    while(i!=n):
        if i==0:
            sum+=p[i+1]
            i+=1
        else:
            if p[i]>i:
                sum+=(p[i]-i)
                i+=1
            else:
                i+=1
    print(sum)
