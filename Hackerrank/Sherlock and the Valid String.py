for _ in range(int(input())):
    s=input()
    word={}
    freq={}
    for i in s:
        if i in word:
            word[i]+=1
        else:
            word[i]=1
    print(word)
    for i in word:
        if word[i] in freq:
            freq[word[i]]+=1
        else:
            freq[word[i]]=1
    print(freq)
    if len(freq)==1:
        print("YES")
    elif len(freq)>2:
        print("NO")
    else:
        l=list(freq)
        if (freq[l[0]]==1 or freq[l[1]]==1):
            if abs(l[0]-l[1])==1:
                print("YES")
            elif (l[0]==1 and freq[l[0]]==1) or (l[1]==1 and freq[l[1]]==1):
                print("YES")
            else:
                print("NO")
        else:
            print('NO')
