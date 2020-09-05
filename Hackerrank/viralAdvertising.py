def viralAdvertising(n):
    x=5
    s=0
    for i in range(n):
       s+=(x//2)
       x=(x//2)*3
    return s
for _ in range(int(input())):
    n=int(input())
    result=viralAdvertising(n)
    print(result)
    
       
