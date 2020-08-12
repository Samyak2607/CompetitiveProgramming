def isprime(n):
    if (n <= 1):
        return False
    if(n <= 3):
        return True
    if (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while(i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True

def hcf(x, y): 
  
   while(y): 
       x, y = y, x % y 
  
   return x

for _ in range(int(input())):
    n,k=map(int,input().split())
    a=list(map(int,input().split()))
    count=0

    if isprime(k):
        print(-1)
    else:
        for i in a:
            if k%hcf(i,k)==0 and k>=i:
                count+=1
        print(count)
        
        
