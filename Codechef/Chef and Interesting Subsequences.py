from math import factorial as f
t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    a.sort()
    l = a[:k]
    x,y=0,0
##    print(x,y)
    temp = max(l)
    for i in a:
        if i == temp:
            x+=1
    for j in l:
        if j == temp:
            y+=1
##    print(x,y)
    print(f(x)//(f(y)*f(x-y)))
    
