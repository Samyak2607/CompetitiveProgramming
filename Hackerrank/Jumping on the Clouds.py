for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    count,i=0,0
    while(i!=n):
        try:
            if a[i+2]==0:
                count+=1
                i+=2
            else:
                i+=1
                count+=1
        except IndexError:
            if i==(n-1):
                count+=1
            break
    print(count)
