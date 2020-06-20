def isprime(num):
    if num > 1: 
        for i in range(2, (num//2)+1):
            if (num % i) == 0:
                return False
        return True
    else: 
        return False

for _ in range(int(input())):
    n=int(input())
    if isprime(n):
        print(-1)
    else:
        if n%10==n:
            print(n)
        else:
            
