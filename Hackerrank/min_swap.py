for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    count,i,j=0,0,n//2
    while((i!=(n//2)-1) and (j!=(n-1))):
        temp_i,temp_j=i,j
        if a[i+1]>a[i]:
            temp=a[i]
            a[i]=a[i+1]
            a[i+1]=temp
            i+=1
            count+=1
        if a[j+1]<a[j]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
            j+=1
            count+=1
        if temp_i==i and temp_j==j:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
            count+=1
    print(count)
            
