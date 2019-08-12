# cook your dish here
import sys

tc=int(input())

for _ in range(tc):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    c=[]
    for i,j in zip(a,b):
        pts=i*20-j*10
        if(pts>0):
            c.append(pts)
        else:
            c.append(0)
    print(max(c))
