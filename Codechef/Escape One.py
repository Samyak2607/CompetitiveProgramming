for _ in range(int(input())):
    n = int(input())
    A = list(map(int, input().split()))
    if A.count(0)==n:
        print(0)
    else:
        for i in range(n-1):
            if A[i]==0:
                continue
            else:
                A[i+1]+=A[i]
                A[i]=0
        if max(A)==1:
            print(-1)
        else:
            print(max(A))
                
