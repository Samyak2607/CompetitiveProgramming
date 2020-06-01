for _ in range(int(input())):
    n = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    a=0
    b=0
    sum=0
    for i,j in zip(A,B):
        if i==j and a==b:
            sum+=i
        a+=i
        b+=j
    print(sum)
