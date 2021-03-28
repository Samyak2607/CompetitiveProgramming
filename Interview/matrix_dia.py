l=[]
for i in range(10):
    temp=list(map(int,input().split()))
    l.append(temp)
ans=0
for i in range(10):
    ans+=l[i][i]
print(ans)
