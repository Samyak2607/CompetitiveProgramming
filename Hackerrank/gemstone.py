for _ in range(int(input())):
    n=int(input())
    a=[]
    for i in range(n):
        a.append(input())
    for i in range(1,n):
        a[i]=set(a[i]).intersection(set(a[i-1]))
    print(len(a[-1]))
