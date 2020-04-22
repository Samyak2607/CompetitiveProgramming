t = int(input())
for _ in range(t):
    n,k = map(int, input().split())
    a = list(map(int,input().split()))
    out_list=[]
    for i in range(n):
        a[i] = a[i]%k
    print(sum(a)%k)
