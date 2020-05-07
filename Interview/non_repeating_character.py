#find the 1st non-repeating character in it and return it's index, otherwise
print('Enter number of test cases')
t = int(input())
for _ in range(t):
    s = input()
    res=-1
    for i in range(len(s)):
        temp = s[i:]
        if temp.count(s[i]) == 1:
            res = s.index(s[i], i,len(s))
            break
    print(res)
    
        
        
