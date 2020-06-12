for _ in range(int(input())):
    std = input()
    l=[]
    pair=0
    
    for s in std:
        if not l:
            l.append(s)
        else:
            if s != l[-1]:
                pair+=1
                del l[:]
            else:
                l.append(s)
    print(pair)
