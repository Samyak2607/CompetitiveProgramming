for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    B=b
    B.extend(a)
    flag,count=0,0
    
    set_a=set(a)
    set_b=set(b)
    if (len(set_a)==len(a)) or (len(set_b)==len(b)):
        if len(set_a)==len(set_b):
            for i in set_a:
                if a.count(i)!=b.count(i):
                    break
                
        elif (len(set_a)==len(a)) and (len(a)%2!=0):
            print(-1)
        elif (len(set_b)==len(b)) and (len(b)%2!=0):
            print(-1)
        else:
            print(0)
    else:
        label:begin
        set_all=set_a|set_b
        both_have=set_a & set_b
        diff=(set_a-set_b)|(set_b-set_a)

        for i in set_all:
            if B.count(i)%2!=0:
                flag=1
                print("1st break")
                break
        if not flag:
            for i in diff:
                if i in a:
                    if a.count(i)%2!=0:
                        flag=1
                        print("2nd break")
                        break
                else:
                    if b.count(i)%2!=0:
                        flag=1
                        print("last break")
                        break
            
        if flag:
            print(-1)
        else:
            for i in both_have:
                count+=abs(a.count(i)-b.count(i))
            print(count)
        

                
        
