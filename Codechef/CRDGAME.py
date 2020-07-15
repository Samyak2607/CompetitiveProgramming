for _ in range(int(input())):
    n=int(input())
    A,B=0,0
    for i in range(n):
        a,b=map(str,input().split())
        if len(a)==1:
            temp=int(a)
        else:
            temp=0
            for j in a:
                temp+=int(j)
        a=temp
        if len(b)==1:
            temp=int(b)
        else:
            temp=0
            for j in b:
                temp+=int(j)
        b=temp
        if a>b:
            A+=1
        elif b>a:
            B+=1
        else:
            A+=1
            B+=1
    if A>B:
        print(0,A)
    elif B>A:
        print(1,B)
    else:
        print(2,A)
    
