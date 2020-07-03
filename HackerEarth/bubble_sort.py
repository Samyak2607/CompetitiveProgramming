def bubble_sort(a):
    count=0
    n=len(a)
    swp=True
    while swp!=False:
        swp=False
        count+=1
        for i in range(0,n-1):
            if a[i]>a[i+1]:
                temp=a[i]
                a[i]=a[i+1]
                a[i+1]=temp
                swp=True
    return count
for _ in range(int(input())):
    a=list(map(int,input().split()))
    print(bubble_sort(a))
