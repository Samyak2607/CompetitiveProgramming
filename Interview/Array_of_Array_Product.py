for _ in range(int(input())):
    arr=list(map(int,input().split()))
    if not arr:
        print(arr)
        continue
    if len(arr)==1:
        print('[]')
        continue
    l=[]
    pro=1
    for i in range(len(arr)):
        l.append(pro)
        pro = pro*arr[i]
    print(l)
    prodval = 1
    for i in range(len(arr)-1,-1, -1):
        l[i] = l[i]*prodval
        print('l[',i,'] ',l[i])
        prodval *= arr[i]
        print('val: ',prodval)
    print(l)
