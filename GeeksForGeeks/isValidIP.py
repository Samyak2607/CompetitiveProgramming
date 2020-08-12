def isValidIP(s):
    #code here
    l=s.split('.')
    for i in l:
        print(i[0])
        if len(i)>3 or len(i)==0:
            return False
        if int(i)>255:
            return False
        if i[0]=='0':
            return False
    return True

for i in range(int(input())):
    s=input()
    print(isValidIP(s))
