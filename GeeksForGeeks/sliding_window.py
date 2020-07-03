for _ in range(int(input())):
    a=list(map(int,input().split()))
    k=int(input())
    l=[]
    n=len(a)

    if k>n:
        print("Invalid")
        continue
    
    for i in range(n):
        print(a[i:i+k])
        if (i+k)>n:
            break
        l.append(sum(a[i:i+k]))
    
    print(max(l))
