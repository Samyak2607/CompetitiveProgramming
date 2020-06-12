for _ in range(int(input())):
    n = int(input())
    coin = list(map(int,input().split()))
    flag=0
    
    if coin[0] != 5:
        print("NO")
        continue
    num=[5]
    coin.pop(0)
    
    for c in coin:
        if c == 5:
            num.append(5)
        elif c == 10:
            if 5 in num:
                num.remove(5)
                num.append(10)
            else:
                flag=1
                break
        else:
            if 10 in num:
                num.append(15)
                num.remove(10)
            elif num.count(5)==2:
                num.append(15)
                num.remove(5)
            else:
                flag=1
                break
    if flag==1:
        print("NO")
    else:
        print("YES")
