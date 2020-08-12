def abbreviation(a, b):
    print(len(a),len(b))
    if len(a)<len(b):
        return 'NO'
    for i in set(b.lower()):
        if i not in a.lower():
            return 'NO'
    i,j,flag=0,0,0
    while(i!=len(a)):
        if (a[i].lower() != b[j]) and (a[i].upper() != b[j]):
            if a[i].islower():
                i+=1
            else:
                flag=1
                print('Reject',a[i],b[j])
                print(i,j)
                break
        else:
            i+=1
            j+=1
            
            if j==len(b):
                break
    if len(a)!=i and flag==0:
        for k in range(i,len(a)):
            if a[k].isupper():
                flag=1
                break
    if len(b)!=j:
        return 'NO'
    if flag:
        return 'NO'
    return 'YES'

for _ in range(int(input())):
    a=input()
    b=input()
    result = abbreviation(a, b)
    print(result)
