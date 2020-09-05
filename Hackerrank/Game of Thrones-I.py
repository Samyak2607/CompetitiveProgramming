for _ in range(int(input())):
    s=input()
    flag=0
    count=0
    l=[]
    for i in s:
        if i not in l:
            if s.count(i)%2!=0:
                count+=1
            if count>1:
                flag=1
                break
            l.append(i)
    if flag:
        print("NO")
    else:
        print("YES")
