for _ in range(int(input())):
    s=input()
    h,m,sec=s[:-2].split(':')
    h=int(h)
    if s[-2:]=='AM':
        if h<12:
            print(s[:-2])
        else:
            h=h+12
            if h>23:
                h='00'
            else:
                h=str(h)
            
    else:
        if h==12:
            print(s[:-2])
        else:
            h=h+12
            if h>23:
                h='00'
            else:
                h=str(h)
            s=h+':'+m+':'+sec
            print(s)
