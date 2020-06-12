for _ in range(int(input())):
    n = int(input())
    ch = list(map(int,input().split()))
    d,m = map(int,input().split())
    count=0
    l=[]
    if len(ch)<m:
        print(0)
    elif len(ch)==1:
        if d==ch[0]:
            print(1)
        else:
            print(0)
    else:
        for s in range(len(ch)-m+1):
            temp=sum(ch[s:s+m])
            if temp==d:
                count+=1
        print(count)
