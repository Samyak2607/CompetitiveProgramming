"""s=input()
d={}

for i in s:
    if i in d:
        d[i]+=1
    else:
        d[i]=1
ans=max(d.values())
count=0
res=''
for i in d:
    if d[i]==ans:
        res=i
        count+=1
if count>1:
    print(0)
else:
    print(res)
"""
"""
def is_prime(n):
    for i in range(2,n//2):
        if n%i==0:
            return False
    return True

n=int(input())
res=1

for i in range(2,n//2):
    if n%i==0:
        if is_prime(i):
            res=i
print(res)
"""
d={}
for i in range(input1):
    a=input2[i]
    b=input3[i]
    if b in d:
        d[b]=max(d[b],a)
    else:
        d[b]=a
return sum(list(d.values()))
