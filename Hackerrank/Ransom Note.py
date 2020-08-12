for _ in range(int(input())):
    m,n=map(int,input().split())
    mag=list(map(str, input().split()))
    note=list(map(str, input().split()))
    flag=0
    
    for i in note:
        if i in mag:
            if note.count(i)>mag.count(i):
                flag=1
                break
        else:
            flag=1
            break
    if flag:
        print("NO")
    else:
        print('YES')
