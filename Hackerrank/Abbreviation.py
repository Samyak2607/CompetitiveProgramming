

def abbreviation(a, b):
    A=a.lower()
    B=b.lower()
    flag=0
    dic={}
    B=b.lower()
    A=a.lower()
    aa=set(a)
    bb=set(b)
    x=''
    if B in A:
        ind=A.index(B)
        end=ind+len(b)-1
        for i in range(len(a)):
            if (i>end) or (i<ind):
                if a[i].isupper():
                    flag=1
                    break
    else:
        if len(a)==len(b):
            return 'NO'
            
        for i in a:
            if (i.lower() not in b) and (i.upper() not in b):
                if i.islower():
                    continue
                else:
                    flag=1
                    break
            else:
                x+=i
        print(x)
        if len(x)<len(b):
            flag=1
        for i in b:
            if (i.lower() not in a) and (i.upper() not in a):
                flag=1
                break
    if flag:
        return 'NO'
    return 'YES'
                



for _ in range(int(input())):
    a=input()
    b=input()
    result = abbreviation(a, b)
    print(result)
