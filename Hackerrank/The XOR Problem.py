for _ in range(int(input())):
    s=input()
    k=int(input())
    count=0
    ans=''
    
    for i in s:
        if i=='0':
            if count<k:
                count+=1
                ans+='1'
            else:
                ans+='0'
        else:
            ans+='0'
    print(ans)
