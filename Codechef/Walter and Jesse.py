t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if max(a)!=max(b):
        print('YES')
    else:
        print('NO')
