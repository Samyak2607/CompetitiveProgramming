def getMoneySpent(k, d, b):
    l=[]
    for i in k:
        for j in d:
            l.append(i+j)
    temp=max(l)
    for i in l:
        if (b-i)<temp and b>i:
            temp=(b-i)
    if temp==max(l):
        return -1
    return (b-temp)
for _ in range(int(input())):
    b,n,m=map(int,input().split())

    k=list(map(int,input().split()))
    d=list(map(int,input().split()))
    result=getMoneySpent(k,d,b)
    print(result)
