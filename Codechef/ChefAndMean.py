import sys

def check(l):
    var=l[0]
    for i in l:
        if(var!=i):
            return False
    return True



q=int(input())

for tc in range(q):
    n=int(input())
    lt=list(map(int, input().split()))
    flag=0
    
    if(check(lt)):
        print(1)

    elif(sum(lt)%n!=0):
        print('Impossible')
    
    else:
        mean=sum(lt)//n
        result=mean*(n-1)
        value=sum(lt)-result
        if(value in lt):
            ans=lt.index(value)
            print(ans+1)
        else:
            print("Impossible")
