for _ in range(int(input())):
    n = int(input())
    l = [0,0,1]
    dict1={'0':2, '1':1}
    if n>3:
        for i in range(3,n):
            if str(l[i-1]) in dict1:
                if dict1[str(l[i-1])]==1:
                    l.append(0)
                    dict1[str(l[i])]+=1
                else:
                    for j in reversed(range(len(l)-1)):
                        if l[j] == l[-1]:
                            temp = len(l)-(j+1)
                            l.append(temp)
                            if str(temp) not in dict1:
                                dict1[str(temp)]=1
                            else:
                                dict1[str(temp)]+=1
    print(l)
    if n==1 or n==0:
        print(n)
    else:
        print(dict1[str(l[n-1])])
