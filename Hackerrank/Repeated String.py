for _ in range(int(input())):
    s=input()
    n=int(input())
    i=0
    x=s.count('a')
    if len(s)==n:
        print(x)
    else:
        temp=n-len(s)
        d=temp//len(s)
        r=temp%len(s)
##        s=s*d+s[:r]
        x=x*(d+1)+s[:r].count('a')
        print(x)
