for _ in range(int(input())):
    n = int(input())
    z=0
    temp=5
    chk=n
    while(chk != 0):
        z+=n//temp
        chk = n//temp
        temp*=5
    print(z)
