for _ in range(int(input())):
    n = int(input())
    
    if n%2!=0:
        for i in range(1,n**2+1):
            if i%n==0:
                print(i)
            else:
                print(i, end=" ")
    else:
        l=[num for num in range(1,n+1)]
        for i in l:
            print(i, end=" ")
        print('')
        temp=0
        j=0
        for i in range(n+1, n**2+1):
            if j%2==0:
                if i%n==0:
                    j+=1
                    print(i-1)
                else:
                    if i%2==0:
                        print(i-1, end=" ")
                    else:
                        print(i+1, end=" ")
            else:
                if i%n==0:
                    j+=1
                    print(i)
                else:
                    print(i, end=" ")
            
                
