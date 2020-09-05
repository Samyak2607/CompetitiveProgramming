def pickingNumbers(a):
    l=[]
    x=list(set(a))
    for i in x:
        if (i+1) in x:
            l.append([i,i+1])
        else:
            l.append([i])
    ans=0
    print(l)
    for i in l:
        temp=0
        for j in i:
            temp+=a.count(j)
        if ans<temp:
            ans=temp
    return ans

for _ in range(int(input())):
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))
    result = pickingNumbers(a)
    print(result)
