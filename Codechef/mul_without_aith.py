def mul(a,b):
    if a==0 or b==0:
        return 0
    if b==1:
        return a
    else:
        return a+mul(a,b-1)
    


for _ in range(int(input())):
    n=int(input())
    n1=int(input())
    print(mul(n,n1))
