for _ in range(int(input())):
    s=input()
    n=int(input())
    l=[]
    x=[]
    dic={}
    for i,j in enumerate(range(97,97+26)):
        dic[chr(j)]=i+1

    for i in range(n):
        l.append(int(input()))
    temp=1
    i=1
    x.append(dic[s[0]])
    while(i!=(len(s))):
        try: 
            if s[i]==s[i+1]:
                x.append(x[-1]+dic[s[i]])
            i+=1
        except IndexError:
            break
        
    print(set(x))
    print(dic)
    for i in range(n):
        if l[i] in x:
            l[i]="YES"
        else:
            l[i]="NO"
    print(l)
                
