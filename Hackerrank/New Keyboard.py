

def is_char(a):
    try:
        int(a)
        return False
    except ValueError:
        return True

for _ in range(int(input())):
    s=input()
    st=[]
    af=False
    ans=''
    lock=True
    key=False
##    for i in s:
##        if i=='*':
##            if not st:
##                continue
##            st.pop()
##            continue
##        if i=='<':
##            af=False
##            key=True
##            continue
##        if i=='>':
##            af=True
##            key=False
##            continue
##        if i=='#':
##            lock= not lock
##            continue
##        if key and lock:
##            ans+=i
##        elif key and (not lock):
##            if is_char(i):
##                ans+=i
##        else:
##            if af:
##                st.insert(0,i)
##            else:
##                st.append(i)
##    while(st):
##        ans+=st.pop()
##    print(ans)
    i=0
    while(s):
        i=s.index('<')
        j=s.index('>')
        for k in range(i+1,j):
            ans+=s.pop(k)
        s.pop(i)
        s.pop(j)
        i=s.index('*')
        try:
            s.pop(i-1)
        except IndexError:
            continue
        
            
        
