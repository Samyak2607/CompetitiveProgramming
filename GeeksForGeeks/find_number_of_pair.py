from itertools import combinations 
def find(a, n): 
    count=0
    pos=[]
    neg=[]
    for i in a:
        if i>=0:
            pos.append(i)
        else:
            neg.append(abs(i)).
    temp=len(pos)
    count = temp*(temp-1)//2
    for i in pos:
        for j in neg:
            if i>j:
                count+=1
    return count

for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    ans=find(a,n)
    print(ans)
