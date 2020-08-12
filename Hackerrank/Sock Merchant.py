for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    x=0
    for i in set(a):
        temp=a.count(i)//2
        x+=temp
    print(x)
