t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    queries = int(input())
    mod = 10**9+7
    for q in range(queries):
        qt = list(map(str,input().split()))
        l = int(qt[1])
        r = int(qt[2])
        if int(qt[0])==1:
            c = qt[3]
            for i in range(l-1, r):
                s = s[0:i]+c+s[i+1:]
        else:
            p = int(qt[3])
            q = int(qt[4])
            for i in range(l-1,r):
                if s[i] == 'A':
                    temp_p = (p-q+mod)%mod
                    temp_q = (p+q)%mod
                    p = temp_p
                    q = temp_q
                elif s[i]=='B':
                    temp_p = (p+q)%mod
                    temp_q = (q-p+mod)%mod
                    p = temp_p
                    q = temp_q
            print(str(p)+" "+str(q))
        
                    
