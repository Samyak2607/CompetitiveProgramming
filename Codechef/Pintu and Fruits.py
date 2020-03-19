t = int(input())
for _ in range(t):
    n,m = map(int,input().split())
    f = list(map(int,input().split()))
    p = list(map(int,input().split()))
    dict = {}
    for i,j in zip(f,p):
        if i not in dict:
            dict[i]=j
        else:
            dict[i]+=j
    print(min(dict.values()))
    
