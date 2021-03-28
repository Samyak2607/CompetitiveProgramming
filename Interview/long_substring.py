n=int(input())
l=[]
for i in range(n):
    pile1=list(map(str,input().split()))
    l.append(pile1)

p2=list(map(str,input().split()))

p2=set(p2)
ind=-1
count=0
d={}
for i in range(n):
    count=0
    count=len(set(l[i]).intersection(p2))
    if count not in d:
        d[count]=i

if not d:
    print(-1)
else:
    mx_k=max(d.keys())
    print(d[mx_k])
        
