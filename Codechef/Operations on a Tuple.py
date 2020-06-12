def check(p,q,r,a,b,c):
    if abs(p)>abs(a):
        temp = abs(p)
        p = abs(a)
        a=temp
    if abs(q)>abs(b):
        temp = abs(q)
        q=abs(b)
        b=temp
    if abs(r)>abs(c):
        temp=abs(r)
        r=abs(c)
        c=temp
    p,q,r,a,b,c=abs(p),abs(q),abs(r),abs(a),abs(b),abs(c)
    
    return (p,q,r,a,b,c)

def mul(p,q,r,a,b,c,count):
    flag=0
    if a%p==0 and b%q==0 and c%r==0:
        temp = min(a//p, b//q)
        if temp==1:
            temp = max(a//p, b//q)
        if min(temp, c//r)==1:
            temp=max(temp,c//r)
        else:
            temp = min(temp,c//r)
        if p!=a:
            p*=temp
        if q!=b:
            q*=temp
        if r!=c:
            r*=temp
        count+=1
    else:
        flag=1
    return (p,q,r,count,flag)
def add(p,q,r,a,b,c,count):
    temp = min(a-p,b-q)
    if temp==0:
        temp=max(a-p,b-q)
    if min(temp,c-r)==0:
        temp=max(temp,c-r)
    else:
        temp=min(temp,c-r)

    if p!=a:
        p+=temp
    if q!=b:
        q+=temp
    if r!=c:
        r+=temp
    count+=1
    return (p,q,r,count)

for _ in range(int(input())):
    p,q,r = map(int,input().split())
    a,b,c = map(int,input().split())
    p,q,r,a,b,c = check(p,q,r,a,b,c)
    count=0
    while(a!=p or b!=q or c!=r):
        if p and q and r:
            p,q,r,count,flag = mul(p,q,r,a,b,c,count)
            if flag:
                p,q,r,count=add(p,q,r,a,b,c,count)
        elif (not p and a) or (not q and b) or (not r and c):
            p,q,r,count=add(p,q,r,a,b,c,count)
        elif p==0 or q==0 or r==0:
            if p==0:
                p=1
                a=1
            if q==0:
                q=1
                b=1
            if r==0:
                r=1
                c=1
            p,q,r,count,flag = mul(p,q,r,a,b,c,count)
            if flag:
                p,q,r,count=add(p,q,r,a,b,c,count)  
        else:
            p,q,r,count=add(p,q,r,a,b,c,count)
    print(count)
            
