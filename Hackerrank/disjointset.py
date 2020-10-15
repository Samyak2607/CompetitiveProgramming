# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=map(int,input().split())
l=list(map(int,input().split()))
a=list(map(int,input().split()))
b=list(map(int,input().split()))
aa=set(l).intersection(set(a))
# print('1st',temp)
bb=set(l).intersection(set(b))
d={}
# print(temp)
count,dic=0,{}

for i in a:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1

for i in l:
    if i in aa:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
for i in aa:
    count+=(max(d[i],dic[i]))
dic={}
d={}
for i in b:
    if i not in dic:
        dic[i]=1
    else:
        dic[i]+=1
for i in l:
    if i in bb:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    

for i in bb:
    count-=(max(d[i],dic[i]))   
print(count)
