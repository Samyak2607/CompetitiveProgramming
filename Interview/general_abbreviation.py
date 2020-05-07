# generate the generalized abbreviation of a input string

t = int(input())
for _ in range(t):
    s = input()
    abbreviation_list=[s]
    for i in range(1,len(s)+1):
        for c in range(len(s)):
            if len(s[:c])+len(s[c+i:])+i==len(s):
                temp = s[:c]+str(i)+s[c+i:]
                abbreviation_list.append(temp)
    print(abbreviation_list)
