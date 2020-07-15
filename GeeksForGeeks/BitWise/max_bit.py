import math

for _ in range(int(input())):
    n=int(input())
    """Method 1"""
    b=bin(n).split('b')[1]
    str='1'
    for i in range(1,len(b)):
        str+='0'
    print(int(str,2))
    """.................................."""

    """Method 2"""

    i=0
    temp=0
    
    while(True):
        if 2**i>n:
            break
        temp=2**i
        i+=1
    print(temp)
    """................................."""

    """ Method 3 """
    if n==0 or n==1:
        print(n)
    else:
        temp=int(math.log(n,2))
        print(2**temp)
        
