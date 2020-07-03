def is_digit(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

for _ in range(int(input())):
    s=input()
    ans=''
    for i in range(s.count('*')):
        j=s.index('*')
        if j==0:
            s=s.replace('*','')
        else:
            s=s[:j-1]+s[j+1:]
    
    lock=False
    for i in range(s.count('#')):
        lock=not lock
        j=s.index('#')
        j=j+1
        if lock:
            while(True):
                try:
                    if s[j]=='#':
                        break
                    if is_digit(s[j]):
                        s=s.replace(s[j],'')
                except IndexError:
                    break
        s=s.replace('#','')
    while(True):
        try:
            if '<' in s:
                i=s.index('<')
                j=s.index('>')
                ans+=s[i+1:j]
                s=s[:i+1]+s[j+1:]
                s=s.replace('<','')
                s=s.replace('>','')
            else:
                break
        except IndexError:
            break
    if s:
        ans+=s
    print(ans)


       
