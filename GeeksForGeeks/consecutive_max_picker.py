for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort(reverse=True)
    sum,i=0,0
    while(True):
        try:
            sum+=a[i]
            if (a[i]-1) in a:
                a.remove(a[i]-1)
            i+=1
            if len(a)==1:
                sum+=a[i]
                break
        except IndexError:
            break
    print(sum)
