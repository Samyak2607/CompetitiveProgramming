import math
for _ in range(int(input())):
    n=int(input())
    l=[2,3,1]
    if n==3:
        print(l)
    elif (int(math.log(n,2))==math.log(n,2)) or n<=2:
        print(-1)
    else:
        i=4
        while(i<=n):
            if i&(i-1)!=0:
                l.append(i)
                i+=1
            else:
                l.append(i+1)
                l.append(i)
                i+=2
        print(l)
        
