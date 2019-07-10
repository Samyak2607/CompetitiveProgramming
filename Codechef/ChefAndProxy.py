q=int(input())

while(q):
    q=q-1
    d=int(input())
    s=input()
    pcount=0
    acount=0
    f=0
    for i in range(0,d):
        if(s[i]=='P'):
            pcount+=1
    if(pcount/d>=0.75):
        print('0')
        continue
    for i in range(2,d-2):
        if(s[i]=='A' and (s[i-1]=='P' or s[i-2]=='P') and (s[i+1]=='P' or s[i+2]=='P')):
            pcount+=1
            acount+=1
            if(pcount/d>=0.75):
                f=1
                print(acount)
                break
    if(f==1):
        continue
    if(pcount/d>=0.75):
        print(acount)
    else:
        print(-1)
    
