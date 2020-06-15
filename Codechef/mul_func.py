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
    P,Q,R = p,q,r
    elif a%p==0 or b%q==0 or c%r==0:
        if a%p==0 and b%q==0 and (a!=p or b!=r):
            temp = min(a//p, b//q)
            if temp==1:
                temp = max(a//p, b//q)
            if p!=a:
                p*=temp
            if q!=b:
                q*=temp
        elif a%p==0 and c%r==0 and (a!=p or c!=r):
            temp = min(a//p, c//r)
            if temp==1:
                temp = max(a//p, c//r)
            if p!=a:
                p*=temp
            if r!=c:
                r*=temp
        elif b%q==0 and c%r==0 and (b!=q or c!=r):
            temp = min(c//r, b//q)
            if temp==1:
                temp = max(c//r, b//q)
            if r!=c:
                r*=temp
            if q!=b:
                q*=temp
        elif a%p==0 and a!=p:
            p*=(a//p)
        elif b%q==0 and b!=q:
            q*=(b//q)
        elif c%r==0 and c!=r:
            r*=(c//r)
    else:
        flag=1
    if P!=p or Q!=q or C!=c:
        count+=1
    return (p,q,r,count,flag)
