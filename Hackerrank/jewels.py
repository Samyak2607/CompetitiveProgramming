for _ in range(int(input())):
    s=input()
    s_set=set(s)
    l=[]
    count=0
##    for i in s_set:
##        if s.count(i)>1:
##            l.append(i)
##            j=0
##            for x in range(count//2):
##                j=s[j:].index(i)
##                k=s[j+1:].index(i)
##                if k=0:
##                    count+=1
##                    s.pop(j)
##                    s.pop(j+1)
##                j+=2
    for i in s_set:
        if s.count(i)>1:
            temp=s.count(i)//2
            for x in range(temp):
                l.append(i)
    print(l)
    for i in l:
        j=s.index(i)
        k=s[j+1:].index(i)+j
        temp=list(set(s[j+1:k]))
        if temp:
            if (len(temp)==1) and (temp[0] in l):
                count+=1
                s=s[:j]+s[j+1:]
                s=s[:k+j]+s[k+j+1:]
                for x in range(s.count(temp[0])):
                    s.replace(temp[0],'')
                count+=(s.count(temp[0])//2)
            else:
                for x in temp:
                    if x not in l:
                        continue
                    l.append(i)
        else:
            s=s[:j]+s[j+1:]
            s=s[:k+j]+s[k+j+1:]
            count+=1
    print(count)
                    
