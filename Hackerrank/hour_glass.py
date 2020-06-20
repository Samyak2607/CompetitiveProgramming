for _ in range(int(input())):
    matrix=[]
    l=[]
    for i in range(6):
        temp=list(map(int,input().split()))
        matrix.append(temp)
    for i in range(4):
        for j in range(4):
            temp=0
            for k in range(3):
                temp+=matrix[i][j+k]+matrix[i+2][j+k]
            temp+=matrix[i+1][j+1]
            l.append(temp)
    print(max(l))
