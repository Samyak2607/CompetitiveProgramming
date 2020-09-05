for _ in range(int(input())):
    s=input()
    ss=set(s)
    flag=0
    if len(ss)==1:
        flag=0
    elif len(s)==2:
        flag=1
        s=s[::-1]
    else: 
        for i in range(len(s)-1,0,-1):
            if s[i]>s[i-1]:
                temp1=s[:i-1]+s[i]+s[i-1]+s[i+1:]
                if s[i+1:]:
                    temp=str(s[i+1:]+s[:i-1]+s[i-1]+s[i])
                    s=min(temp1,temp)
                else:
                    s=temp1
                flag=1
                break
        temp=s
        for i in range(len(s)-1,0,-1):
            for j in range(i-1,0,-1):
                if s[i]>s[j]:
                    s=s[:
        
    if flag:
        print(s)
    else:
        print('no answer')
