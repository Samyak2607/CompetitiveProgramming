for _ in range(int(input())):
    s=input()
    word='gfg'
    count=0
    i=0
    while(True):
        if word in s[i:]:
            count+=1
            i=s[i:].index(word)+1+i
            if i>=len(s):
                break
        else:
            break
    if count==0:
        print(-1)
    else:
        print(count)
