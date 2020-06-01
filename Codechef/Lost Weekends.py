for _ in range(int(input())):
    work = list(map(int,input().split()))
    p = work[-1]
    work = work[:-1]
    if ((p*sum(work))//5) > 24:
        print("Yes")
    else:
        print("No")
