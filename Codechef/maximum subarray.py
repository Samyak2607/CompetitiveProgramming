t = int(input())
for _ in range(t):
    n = list(map(int,input().split()))
    max_list=[]
    for i in n:
        if not max_list:
            max_list.append(i)
            prev = i
        else:
            prev = max(prev+i, i)
            max_list.append(prev)
    print(max(max_list))
