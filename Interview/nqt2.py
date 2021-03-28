l=[0.00,0.04,0.09,0.15,0.19,0.22]
t=float(input())
if t>=24 or t<0:
    print('INVALID INPUT')
else:
    for i in l:
        print(i+t,end=' ')
