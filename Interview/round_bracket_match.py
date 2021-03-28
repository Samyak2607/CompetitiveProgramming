s=input()
l=[]
flag=0
for i in s:
    if i==')' and len(l)==0:
        flag=1
        break
    if i=='(':
        l.append(i)
    elif i==')':
        l.pop()
if flag:
    print(1)
elif len(l)!=0:
    print(1)
else:
    print(0)
        
