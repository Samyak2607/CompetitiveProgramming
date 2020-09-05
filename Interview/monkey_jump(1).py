for _ in range(int(input())):
    l=list(map(int,input().split()))
    i,count=l[0],0
    while(i<len(l)):
        try:
            i=l[i]
            l=l[i:]
            count+=1
        except IndexError:
            count+=1
            break
    print(count)
            
            
