for _ in range(int(input())):
    n = int(input())
    goal = input()
    a,b,flag=0,0,0
    for i in range(2*n):
        temp = int(goal[i])
        if i%2==0:
            a+=temp
        else:
            b+=temp
        a_temp = (2*n-i-1)//2
        b_temp = 2*n-i-1-a_temp

        if a>b_temp+b:
            flag=i+1
        elif b>a_temp+a:
            flag=i+1
    print(flag)
    
        
    
