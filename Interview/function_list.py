def num(i):
    l=[0,1]
    if i==1:
        return l[1]
    else:
        for j in range(2,i+1):
            temp=3*l[j-1]-2*l[j-2]
            l.append(temp)
        return l[-1]

def is_part_of_series(lst):
    x={}
    for i in lst:
        if i not in x:
            result=num(i)
            x[i]=result
    return list(x.values())
a=list(map(int,input().split()))
print(is_part_of_series(a))
        
        
