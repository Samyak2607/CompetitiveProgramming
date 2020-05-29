for _ in range(int(input())):
    word = input()
    l = len(word)
    flag=0
    if l%2 == 0:
        temp1 = word[:l//2]
        temp2 = word[l//2:]
    else:
        temp1 = word[:l//2]
        temp2 = word[l//2 + 1:]
    word_list = list(set(temp1))
    for c in word_list:
        if temp1.count(c) != temp2.count(c):
            flag=1
            break
    if flag == 0:
        print("YES")
    else:
        print("NO")
