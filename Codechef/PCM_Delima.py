import operator
t = int(input())

for _ in range(t):
    n,w,x,y = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    dict1 = {}
    result =0
    for i,j in zip(a,b):
        if i not in dict1:
            dict1[i] = j
        else:
            temp = max(dict1[i],j)
            dict1[i] = temp
    sorted_d = dict( sorted(dict1.items(), key=operator.itemgetter(1),reverse=True))
    l = list()
    for i,j in sorted_d.items():
        if i<=w:
            temp = max(x,y)
            result = temp*j
            l.append(i)
            break
    for i,j in sorted_d.items():
        temp = w-sorted_d[i]
        if i<=temp and i not in l:
            result+=min(x,y)*sorted_d[i]
            break
    print(result)
    
    
    
    
        
