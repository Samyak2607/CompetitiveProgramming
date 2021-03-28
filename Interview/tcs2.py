"""s=input()
l=[]
for i in s:
    l.append(ord(i))

ans=l[0]

for i in range(1,len(l)):
    ans^=l[i]
print(ans)    
"""

n=int(input())
d={}
l=[]

for i in range(n):
    num=int(input())
    l.append(num)
if len(l)==len(set(l)):
    print(l[0])
else:
    flag=0
    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    for i in d:
        d[i]==1:
            print(i)
            flag=1
            break
    if flag==0:
        print(-1)
    
    
        
