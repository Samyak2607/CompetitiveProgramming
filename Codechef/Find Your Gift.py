def grid(j, x, y):
    if j=='L':
        x-=1
    elif j=='R':
        x+=1
    elif j=='U':
        y+=1
    else:
        y-=1
    return (x,y)
for _ in range(int(input())):
    n=int(input())
    s = input()
    l=[]
    dict1={}
    x,y=0,0
    dict1['L']=0
    dict1['R']=0
    dict1['U']=1
    dict1['D']=1
    
    for i in range(n):
        if not l:
            l.append(s[i])
            x,y=grid(s[i],x,y)
        else:
            if dict1[s[i]]==dict1[l[-1]]:
                continue
            else:
                l.append(s[i])
                x,y=grid(s[i],x,y)
    print(x,y)
                
