t = int(input())
for _ in range(t):
    a,b = map(str, input().split())
    if (len(a)==1 and len(b)==1):
        print(int(a)+int(b))
    elif(len(a)==1):
        if int(a)>int(b[0]):
            print(int(a)*10+int(b[1])+int(b[0]))
        else:
            print(int(a)+int(b))
    elif(len(b)==1):
        if int(b)>int(a[0]):
            print(int(b)*10+int(a[1])+int(a[0]))
        else:
            print(int(a)+int(b))
    else:
        print(max(int(a)+int(b),int(b[0]+a[1])+int(a[0]+b[1]),int(b[1]+a[1])+int(b[0]+a[0]),int(a[0]+b[0])+int(a[1]+b[1])))
