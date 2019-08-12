t=int(input())
for _ in range(t):
    n,k=input().split()
    n=int(n)
    k=int(k)
    if(n%(k*k)==0):
        print("NO")
    else:
        print("YES")
