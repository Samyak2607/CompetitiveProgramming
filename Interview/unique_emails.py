def unique_email(emails):
    count=0
    name_dic={}
    domain={}
    for i in emails:
        name=i.split('@')
        if name[1] in domain:
            name=name[0].split('+')
            name=name[0].split('.')
            name=''.join(name)
            if name not in name_dic:
                name_dic[name]=0
                count+=1
                print(name)
        else:
            print(i)
            domain[name[1]]=0
            name=name[0].split('+')
            name=name[0].split('.')
            name=''.join(name)
            name_dic[name]=0
            count+=1
    return count

for _ in range(int(input())):
    emails=list(map(str,input().split()))
    print(unique_email(emails))
