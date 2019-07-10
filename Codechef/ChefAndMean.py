# cook your dish9 here
import sys

q=int(input())

for tc in range(q):
    n=int(input())
    lt=list(map(int, input().split()))
    mean=sum(lt)/len(lt)
    l=len(lt)
    flag=0
    
    for i in range(0, l):
        temp=lt[i]
        lt.remove(lt[i])
        mean1=sum(lt)/len(lt)
        if(mean == mean1):
            flag=1
            print(i+1)
            break
        lt.insert(i,temp)
    if(flag==0):
        print('Impossible')
    
