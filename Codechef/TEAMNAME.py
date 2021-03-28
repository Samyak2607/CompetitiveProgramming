for _ in range(int(input())):
    n=int(input())
    l=list(map(str,input().split()))

    f=set()
    ln=set()

    for i in l:
        
        f.add(str(i[0]))
        ln.add(str(i[1:]))
    
    print(len(ln)*(len(f)-1))
    
