def posOfRightMostDiffBit(m,n):
    #Your code here
    if n==m:
        return -1
    if n&1!=m&1:
        return 1
    if m<n:
        temp=n
        n=m
        m=temp
    m=(bin(m).split('b')[1])[::-1]
    n=bin(n).split('b')[1][::-1]
    
    for i in range(len(n)):
        if m[i]!=n[i]:
            return i+1
    for i in range(len(n),len(m)):
        if m[i]=='1':
            return i+1

for _ in range(int(input())):
    m,n=map(int,input().split())
    
    print(posOfRightMostDiffBit(m,n))
        
