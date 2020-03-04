t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))
    sum=0
    a.sort()
    b.sort()
    for i,j in zip(a,b):
        sum+=min(i,j)
    print(sum)
