def countone(n): 
      
    count0, count1 = 0, 0
    while (n != 0): 
      
        # calculating count of zeros and ones 
        if(n % 2 == 0):  
            count0 += 1
        else: 
            count1 += 1
        n //= 2
        
    return (count1)

t = int(input())
for _ in range(t):
    n,q = map(int. input().split())
    a = list(map(int, input().split()))
    for i in range(q):
        
