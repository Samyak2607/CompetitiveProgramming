for _ in range(int(input())):
    n=int(input())
    b=bin(n).split('b')[1]
    n1='1'*len(b)
    n1=int(n1,2)
    n2=n^n1
    res=n1*n2
    while(True):
        n1-=1
        if n1==n2:
            break
        if n1==n:
            n1-=1
        n2=n^n1
        if res<n1*n2:
            res=n1*n2
        else n1*n2==0:
            break
        
    print(res)
