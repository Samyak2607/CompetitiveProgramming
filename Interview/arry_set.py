for _ in range(int(input())):
    s=input()
    if s==s[::-1]:
        print("YES")
    else:
        l=list(s)
        dic={}
        for i in l:
            if i in dic:
                dic[i]+=1
            else:
                dic[i]=1
                
        if len(l)%2==0:
            flag=0
            for i in dic:
                if dic[i]%2!=0:
                    
                    flag=1
                    break
            if flag:
                print("NO")
            else:
                print("YES")
        else:
            count=0
            for i in dic:
                if dic[i]%2!=0:
                    count+=1
            if count%2==0:
                print("NO")
            else:
                print("YES")
            
            
            
    
