for _ in range(int(input())):
    n=int(input())
    if n&(n-1)==0:
        print("Power of 2")
    else:
        print("Not a power of 2")
