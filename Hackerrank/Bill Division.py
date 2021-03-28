def bonAppetit(bill, k, b):
    temp=sum(bill)
    temp=temp-bill[k]
    if temp//2==b:
        return 'Bon Appetit'
    
    return abs((temp//2)-b)

for _ in range(int(input())):
    n,k=map(int,input().split())
    bill=list(map(int,input().split()))
    b=int(input())
    res=bonAppetit(bill, k, b)
    print(res)
