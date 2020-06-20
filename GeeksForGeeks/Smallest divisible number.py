def gcd(a,b): 
    if a == 0: 
        return b 
    return gcd(b % a, a)

def lcm(a,b): 
    return (a*b)//gcd(a,b)

for _ in range(int(input())):
    n=int(input())
    temp=2
    for i in range(3,n+1):
        temp=lcm(temp,i)
    print(temp)
