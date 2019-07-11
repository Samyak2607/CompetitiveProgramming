import sys

n,k = map(int,input().split())
l=list(0 for z in range(n))
count=0
for i in range(k):
        temp=input()
        if(temp=='CLOSEALL'):
            l=list(0 for i in range(n))
            count=0
        else:
            num=temp.split()[-1]
            num=int(num)
            if(l[num-1] == 1):
                l[num-1]=0
                count=count-1
            else:
                l[num-1]=1
                count+=1
        print(count)    
        



    
