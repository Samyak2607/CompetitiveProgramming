for _ in range(int(input())):
    l=list(map(int,input().split()))
    i=0
    count=0
    while(i!=len(l) or l!=l[-1]):
        i=l[i]
        count+=1
    print(count)
