def quartile(x,n):
    temp=n//2
    if (temp)%2==0:
        q1=(x[temp//2]+x[(temp//2)-1])//2
        q1=float('%.1f'%q1)
    else:
        q1=x[temp//2]
        q1=float('%.1f'%q1)
    temp=n//2
    if (temp)%2==0:
        q3=(x[n-(temp//2)-1]+x[n-temp//2])//2
        q3=float('%.1f'%q3)
    else:
        q3=x[n-(temp//2)-1]
        q3=float('%.1f'%q3)
    
    return (q3-q1)


n=int(input())
x = list(map(int,input().split()))
f=list(map(int,input().split()))
q={}
for i,j in zip(x,f):
    if i in q:
        q[i]+=j
    else:
        q[i]=j
num=sum(f)
l=[]
for i in sorted(q.keys()):
    l.extend(list([i])*q[i])
print(quartile(l,num))
