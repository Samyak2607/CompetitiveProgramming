a=int(input())
b=int(input())

inte=0
exte=0
ans=0
for i in range(n):
    temp=float(input())
    inte+=temp
inte*=18
for i in range(m):
    temp=float(input())
    exte+=temp
exte*=12
ans=inte+exte
print(ans)
    
