def beautifulDays(a, b, k):
    l=[]
    mat=[]
    for i in range(a,b+1):
        l.append(i)
    mat=list(l)
    for i in range(len(l)):
        mat[i]=int(str(l[i])[::-1])   
    count=0
    for i,j in zip(l,mat):
        if abs(i-j)%k==0:
            count+=1
    return count

for _ in range(int(input())):
    a,b,k=map(int,input().split())
    result=beautifulDays(a, b, k)
    print(result)
