for _ in range(int(input())):
    n = int(input())
    speed = list(map(int, input().split()))
    count=1
    for i in range(1,len(speed)):
        if speed[i]<= speed[i-1]:
            count+=1
    print(count)
