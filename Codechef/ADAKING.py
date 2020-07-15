for _ in range(int(input())):
    k=int(input())
    matrix=[]
    count=0
    for i in range(8):
        l=[]
        for j in range(8):
            l.append('X')
        matrix.append(l)
    for i in range(8):
        for j in range(8):
            count+=1
            if count<=k:
                matrix[i][j]='.'
    matrix[0][0]='O'
    for i in range(8):
        for j in range(8):
            print(matrix[i][j],end='')
        print('')
    
            
