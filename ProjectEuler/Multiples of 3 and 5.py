for _ in range(int(input())):
    n=int(input())
    sum=0
    rem=n%10
    if rem==0:
        n=(n//10)-1
        rem=10
    else:
        n=n//10
    count=0
    l=[23,15,17]
    for i in range(n):
        if count==3:
            count=0
        temp=int(str(l[count])[0])
        if count%2==0:
            temp2=i*4 
        else:
            temp2=i*3
        temp+=temp2
        temp=str(temp)+str(l[count])[-1]
        sum+=(int(temp)+(i+1)*10)
        count+=1
    temp=0
    """
    for i in range(1,rem):
        if (i%3==0) or (i%5==0):
            temp+=i
        
    if count==3:
        count=0
    temp2=0
    if count%2==0:
        temp2=temp//10+n*4
    else:
        temp2=temp//10+n*3
    temp=int(str(temp2)+str(temp%10))
    sum+=temp
    """
    for i in range(1,rem):
        x=n*10+i
        if (x%3==0) or (x%5==0):
            sum+=x
    print(sum)
