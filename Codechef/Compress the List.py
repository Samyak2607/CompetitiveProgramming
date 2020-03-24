t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    i,j=0,0
    count=0
    output=''
    flag=0
    l =[]
    while(i!=n):
        if not l:
            l.append(a[i])
            j+=1
            if j == n:
                output+=str(a[i])+','
        else:
            if a[i] == l[-1]+1:
                l.append(a[i])
                j+=1
                if j==n:
                    for y in l:
                        output+=str(y)+','
            elif len(l)>2:
                output+=str(l[0])
                output+='...'
                output+=str(l[-1])+','
                del l[:]
            else:
                if len(l)<3:
                    if (a[i]-l[-1])>1:
                        flag=1
                    for y in l:
                        output+=str(y)+','
                    del l[:]
                if flag:
                    j+=1
                    l.append(a[i])
                    if j==n:
                        for y in l:
                            output+=str(y)+','
        
        i=j
    print(output[:-1])
