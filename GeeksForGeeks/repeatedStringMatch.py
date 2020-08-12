def repeatedStringMatch(A,B):
    # code here
    a=set(A)
    b=set(B)
    flag=0
    count=0
    if len(a)>len(b):
        for i in a:
            if i not in b:
                flag=1
    else:
        for i in b:
            if i not in a:
                flag=1
    if flag:
        return -1
    if (A not in B) and (B not in A):
        return -1
    if B in A:
        return 1
    if len(A)>len(B):
        return -1
    temp=(len(A)+len(B)+len(A))
    while(len(A)<temp):
        if B in A:
            break
        A+=A
        count+=1
    if B not in A:
        return -1
    return count+1


for _ in range(int(input())):
    A=input()
    B=input()
    print(repeatedStringMatch(A,B))
