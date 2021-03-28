s=input()
b=s[1:]+s[0]
f=s[-1]+s[:-1]
if b==f:
    print(1)
else:
    print(0)
