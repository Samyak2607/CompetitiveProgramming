for _ in range(int(input())):
    s=input()
    count=0
    if s[0]=='1':
        count=1
    for i in range(len(s)-1):
        if s[i]!=s[i+1] and (s[i+1]=='1'):
            count+=1
    print(count)
