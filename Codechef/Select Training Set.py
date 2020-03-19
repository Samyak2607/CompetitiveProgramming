t = int(input())
for _ in range(t):
    n = int(input())
    dict_0={}
    dict_1={}
    count=0
    set1 = set()
    for i in range(n):
        s,b = map(str, input().split())
        set1.add(s)
        if b == '0':
            if s in dict_0:
                dict_0[s]+=1
            else:
                dict_0[s]=1
                dict_1[s]=0
        else:
            if s in dict_1:
                dict_1[s]+=1
            else:
                dict_1[s]=1
                dict_0[s]=0
    for i in set1:
        temp = max(dict_0[i],dict_1[i])
        count+=temp
    print(count)
