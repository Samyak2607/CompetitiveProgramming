tc=int(input())

for _ in range(tc):
    n=input()
    l=list(map(int,input().split()))
    n=int(n[0])
    ans=[]
    res=[]
    if len(l)<=2:
        print(max(a))
        continue
    a=list(set(l))
    if len(a)==1:
        print(a[0]*(len(l)//2)+a[0]*(len(l)%2)) 
        continue
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            temp=a[i]+a[j]
            ans.append(temp)
    
    if len(set(ans))==len(ans):
        print(min(ans))
    else:
        for i in set(ans):
            if ans.count(i)>1:
                res.append(i)
        
        if len(res)!=0:
            print(min(res))
        else:
            print(min(ans))
            
