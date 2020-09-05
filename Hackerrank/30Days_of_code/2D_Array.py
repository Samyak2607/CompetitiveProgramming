for _ in range(int(input())):
    mat=[]
    x=[]
    for i in range(6):
        l=list(map(int,input().split()))
        mat.append(l)
    ans=-1
    for i in range(4):
        temp=0
        for j in range(4):
            temp=mat[i+1][j+1]
            for k in range(3):
                temp+=mat[i][j+k]+mat[i+2][j+k]
            if ans<temp:
                ans=temp
        
    print(ans)
