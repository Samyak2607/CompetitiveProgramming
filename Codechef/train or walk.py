t = int(input())
for _ in range(t):
    n,A,B,C,D,p,q,y = map(int, input().split())
    x = list(map(int, input().split()))
    a = x[A-1]
    b = x[B-1]
    c = x[C-1]
    d = x[D-1]
    walk = p*(abs(b-a))
    if p*abs(c-a) <= y:
        train = y+q*abs(c-d)+p*abs(d-b)
    else:
        train = walk
    print(min(walk,train))
