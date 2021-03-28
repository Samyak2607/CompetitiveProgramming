def std_clk(t,zone):
    t=t.split(':')
    h=int(t[0])
    m=int(t[1])
    if h==12 and zone=='AM':
        h=0
    elif zone=='PM' and h!=12:
        h+=12
    m=m/60
    h+=m

    return h
    

for _ in range(int(input())):
    p=input()
    n=int(input())
    
    p=p.split()
    p=std_clk(p[0],p[1])

    ans=''
    
    for i in range(n):
        t=input().split()
        t1=std_clk(t[0],t[1])
        t2=std_clk(t[2],t[3])

        if p>=t1 and p<=t2:
            ans+='1'
        else:
            ans+='0'
    print(ans)
        
