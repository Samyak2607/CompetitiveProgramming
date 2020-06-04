for _ in range(int(input())):
    n = int(input())
    l=[]
    for i in range(n):
        s,p,v = map(int,input().split())
        temp = p//(s+1)
        l.append(temp*v)
    print(max(l))
