for i in range(int(input())):
    n,q = map(int,input().split())
    s = input()
    res=[]
    for i in range(q):
        c = int(input())
        temp=0
        l = []
        for v in s:
            if (s.count(v)-c)>0 and (v not in l):
                temp+=(s.count(v)-c)
                l.append(v)
        print(temp)

