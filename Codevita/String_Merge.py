for _ in range(int(input())):
    s=input()
    n=int(input())
    dic={}
    temp=''
    flag=0
    com=[]
    for i in s:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    
    for i in range(n):
        x=input()
        temp+=x
        l.append(x)
    if len(temp)!=len(s):
        flag=1
    else:
        for i in l:
            if i not in s:
                
                
    if flag:
        print("NO")
    else:
        print("YES")
