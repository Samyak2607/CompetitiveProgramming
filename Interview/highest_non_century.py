l=[]
while(True):
    n=int(input())
    if n<0:
        break
    l.append(n)
ans=0
a=[]
for i in range(len(l)-1):
    if l[i]%2==0 and l[i+1]%2==0:
        a.append(l[i]+l[i+1])
    else:
        if l[i]%2==0:
            a.append(l[i])
        elif l[i+1]%2==0:
            a.append(l[i+1])
a.sort(reverse=True)
count=0
if a[0]>20:
    print(1)
else:
    for i in a:
        ans+=i
        if ans>20:
            count=count+1
            break
        count+=1
    print(count)
        
    
