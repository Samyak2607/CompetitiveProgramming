for i in range(int(input())):
    n = int(input())
    x = list(map(int, input().split()))
    count=1
    infected_person=[]
    for i in range(1,len(x)):
        if (x[i]-x[i-1])<=2:
            count+=1
        else:
            infected_person.append(count)
            count=1
    if count!=1:
        infected_person.append(count)
    elif len(x)==1:
        infected_person.append(1)
    print(min(infected_person), max(infected_person))
