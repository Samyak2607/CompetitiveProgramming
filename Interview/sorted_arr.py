n=int(input())
a=list(map(int,input().split()))
m=max(a)



a.sort(reverse=True)
ans=sum(a[:2])
print(ans)
