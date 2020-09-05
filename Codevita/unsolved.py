for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))

    temp=max(a)
    temp=len(bin(temp).split('b')[1])
    for i in a:
        x=bin(i).split('b')[1]
        p=temp-len(x)
        if p!=0:
            x='0'*p+x
            
        b.append(x)
    for i in b:
        lnot=b[i].count('0')
        l1=b[i].count('1')
        sum1+=l1
        sum0+=lnot
        if sum1==sum0:
            count+=1
    for i,j in zip(lnot,l1):
        
        
