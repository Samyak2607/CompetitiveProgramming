for _ in range(int(input())):
    n,m = map(int,input().split())
    l=list(map(int,input().split()))
    ans=[]
    i,j=0,0
    while(len(l)!=0):
        if i!=(n-1):
            print("In IF part")
            temp=l.pop(i)
            ans.append(temp)
            i+=1
            print(temp,i)
        else:
            print("Else part now")
            if j!=(m-1):
                i+=n
                temp=l.pop(i)
                ans.append(temp)
                j+=1
                print(temp,i)
            else:
                l.reverse()
                n-=1
                m-=1
                i=0
                j=0
                
    print(ans)
