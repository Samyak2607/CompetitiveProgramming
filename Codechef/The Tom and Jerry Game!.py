for _ in range(int(input())):
    ts = int(input())
    ch=0
    if ts%2==0:
        while(ts%2 == 0):
            ts = ts//2
    temp = ts//10
    ch=temp*5
    ts = ts%10
    for i in range(1,ts):
        if i%2==0:
            ch+=1
    print(ch)
