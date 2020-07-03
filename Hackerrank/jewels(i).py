def pop(s,ind):
    s=s[:ind]+s[ind+1:]
    return s
for _ in range(int(input())):
    s=input()
    s+='*'
    count,i=0,1
    while(True):
        if s[i]=='*':
            break
        if s[i]==s[i-1]:
            s=pop(s,i-1)
            s=pop(s,i-1)
            i=i-1
            count+=1
        elif s[i]==s[i+1]:
            s=pop(s,i)
            s=pop(s,i)
            count+=1
        else:
            i+=1
            if s[i]=="*":
                break
    print(count)
            
