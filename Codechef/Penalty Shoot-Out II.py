for _ in range(int(input())):
    n = int(input())
    goal = input()
    a=0
    b=0
    flag=0
    for i in range(2*n):
        temp = int(goal[i])
        if i%2==0:
            a+=temp
        else:
            b+=temp
            if a>b:
                if a>(b+n-(i+1)//2):
                    flag=i+1
                    break
            elif b>a:
                if b>(a+n-(i+1)//2):
                    flag=i+1
                    break
            else:
                flag=i+1
    print(flag)
        
            
        
