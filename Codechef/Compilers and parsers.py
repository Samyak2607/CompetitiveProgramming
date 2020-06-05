for _ in range(int(input())):
    exp = input()
    stc=[]
    l=[]
    pop=0
    if exp[0]=='>':
        print(0)
        continue
    for sym in exp:
        if sym=='<':
            stc.append(sym)
            l.append(pop)
            pop=0
        else:
            if not stc:
                l.append(pop)
                pop=0
                continue
            stc.pop()
            pop+=1
    l.append(pop)
    print(2*max(l))
