for _ in range(int(input())):
    a=list(map(int,input().split()))

    ev,odd=a[0],a[1]
    l=[]
    for i in range(2,len(a)):
        if i%2==0:
            ev+=a[i]
            if l:
                if l[-1]<=ev:
                    l.append(ev)
                else:
                    ev=0
            else:
                l.append(ev)
        else:
            odd+=a[i]
            if l:
                if l[-1]<=odd:
                    l.append(odd)
                else:
                    odd=0
            else:
                l.append(odd)
    print(max(l))
            
