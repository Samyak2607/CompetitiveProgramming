from collections import defaultdict
for _ in range(int(input())):
    flag = 0
    n,m = map(int,input().split())
    graph = defaultdict(list)
    for i in range(m):
        u,v,w = map(int,input().split())
        graph[u].append([v,w])
        graph[v].append([u,-1*w])
    print(graph.keys())
    for i in graph.keys():
        temp = graph[i][0][0]
        sum = graph[i][0][1]
        temp1=i
        sum_chk=0
        l=[i,temp]
        while(temp1!=temp):
            if graph[temp1][0][0] not in l:
                temp1 = graph[temp1][0][0]
                sum_chk+=graph[temp1][0][1]
                l.append(temp1)
            else:
                temp1 = graph[temp1][1][0]
                sum_chk+=graph[temp1][1][1]
                l.append(temp1)
        if sum != sum_chk:
            flag=1
            break
    if flag==0:
        print("YES")
    else:
        print("NO")
    
            
