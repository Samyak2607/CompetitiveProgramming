for _ in range(int(input())):
    n=int(input())
    a=[]
    dic={}
    for p in range(n):
        a.append(int(input()))
    x=1
    dic[0]=1
    for i in range(1,n):
        if a[i]>a[i-1]:
            dic[i]=dic[i-1]+1
        elif a[i]==a[i-1]:
            dic[i]=1
        else:
            if dic[i-1]>3:
                dic[i]=dic[i-1]//2
            else:
                dic[i]=1
    print(list(dic.values()))
    print(sum(list(dic.values())))
            
