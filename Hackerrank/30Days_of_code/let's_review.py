for _ in range(int(input())):
    s=input()
    ev,od='',''
    for i in range(len(s)):
        if i%2==0:
            ev+=s[i]
        else:
            od+=s[i]
    print(ev,od)
