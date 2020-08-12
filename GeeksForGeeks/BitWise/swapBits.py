def swapBits(n):
    s=''
    x=bin(n).split('b')[1]
    if len(x)%2!=0:
        x='0'+x[:]
    for i in range(len(x)-1,0,-2):
        s=x[i]+x[i-1]+s
    return int(s,2)

for _ in range(int(input())):
    n=int(input())
    print(swapBits(n))
