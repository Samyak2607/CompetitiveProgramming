def sumBitDiff(a,n):
    l=[]
    count=0
    for i in range(n):
        for j in range(n):
            l.append(a[i]^a[j])
    print(l)
    for i in l:
        temp=bin(i).split('b')[1].count('1')
        count+=temp
    return count
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    print(sumBitDiff(a,n))
