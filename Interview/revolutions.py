for _ in range(int(input())):
    r1,r2,r3=map(int,input().split())
    v1,v2,v3=map(int,input().split())
    n=int(input())
    w1=float(str(v1/r1)[:3])
    w2=float(str(v2/r2)[:3])
    w3=float(str(v3/r3)[:3])
    if w1==w2 and w2==w3:
        print(True)
    else:
        print(False)
