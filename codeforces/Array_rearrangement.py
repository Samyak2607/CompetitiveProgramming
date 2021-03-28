tc=int(input())
tc+=(tc-1)
for _ in range(tc):
    try:
        n,x=map(int,input().split())
        a=list(map(int,input().split()))
        b=list(map(int,input().split()))
        a.sort(reverse=True)
        b.sort(reverse=True)
        i,j,flag=0,0,0
        
        while(True):
            try:
                if j==n:
                    break
                elif (a[i]+b[j])<=x:
                    
                    a.pop(i)
                    b.pop(j)
                    i,j=0,0
                else:
                    if (len(a)==0 and len(b)==0):
                        flag=1
                        break
                    else:
                        j+=1
            except IndexError:
                if (len(a)==0 and len(b)==0):
                    flag=1
                break
        if flag:
            print("Yes")

        else:
            print("No")
    except ValueError:
        continue
