for _ in range(int(input())):
    n,m=map(int,input().split())
    q,l=[],[]
    for i in range(n):
        l.append(0)
    for i in range(m):
        q.append(list(map(int, input().rstrip().split())))
    print(q)
    for i in q:
        print(i[0],i[1],i[2])
