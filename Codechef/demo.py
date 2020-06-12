temp=0
l=[1,2]
even=[2]
for i in range(2,100):
    l.append(l[i-1]+l[i-2])
    if l[i]%2==0:
        even.append(l[i])
print(even)
diff=[]
for i in range(1,len(even)):
    diff.append(even[i]-even[i-1])
print(diff)
diff2=[]
for i in range(1,len(diff)):
    diff2.append(diff[i]-diff[i-1])
print('diff2: ',diff2)
