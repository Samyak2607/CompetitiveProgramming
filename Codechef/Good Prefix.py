t = int(input())
for _ in range(t):
    s = input()
    k,x = map(int,input().split())
    count=0
    sum=0
    l={}
    for i in s:
        if i not in l:
            l[i]=1
        else:
            if x>l[i]:
                l[i]+=1
            elif k:
                k-=1
                count+=1
                continue
            else:
                break
    for i in l.values():
        sum+=i
    print(sum)
    
                
