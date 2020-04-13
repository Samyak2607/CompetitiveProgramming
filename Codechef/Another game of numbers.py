t = int(input())
for _ in range(t):
    a,b = map(int,input().split())
    bin_a = bin(a).split('b')[1]
    bin_b = bin(b).split('b')[1]
    out=[]
    count=0
    l=[]
    temp_out = a^b
    if len(bin_a)>len(bin_b):
        diff = len(bin_a)-len(bin_b)
        for i in range(diff):
            bin_b = '0'+bin_b
    
    if len(bin_a)<len(bin_b):
        diff = len(bin_b)-len(bin_a)
        for i in range(diff):
            bin_a = '0'+bin_a
    if (bin_b.count('1') == len(bin_b)) or (bin_b.count('0')== len(bin_b)):
        print(0,int(bin_a,2)^int(bin_b,2))
    else:
        while(count!=len(bin_b)):
            bin_b = bin_b[-1]+bin_b[0:-1]
            count+=1
            temp = int(bin_a,2)^int(bin_b,2)
            out.append(temp)
        if temp_out>max(out):
            print(0,temp_out)
        else:
            print(out.index(max(out))+1,max(out))
