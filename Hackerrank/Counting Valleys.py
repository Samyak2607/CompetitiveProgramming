for _ in range(int(input())):
    n = int(input())
    s = input()
    hill,valley=0,0
    for i in s:
        if i=='D':
            hill-=1
        elif i=='U':
            hill+=1
            if hill==0:
                valley+=1
    print(valley)
