print("For Example : abc+* should be entered as a b c + *")
for _ in range(int(input("Enter Number of Test you wanna Test: "))):
    inp=input("Enter postfix expression  with space:  ")
    lst=inp.split(" ")
    operator=['+','-','/','*','^']
    operands=[]
    a=1
    for i in lst:
        if(i not in operator):
            operands.insert(0,i)
        else:
            if(len(operands)>=2):
                num1=operands.pop(0)
                num2=operands.pop(0)
                num1=int(num1)
                num2=int(num2)
                if(i=='*'):
                    operands.insert(0,num2*num1)
                elif(i=='/'):
                    operands.insert(0,num2/num1)
                elif(i=='+'):
                    operands.insert(0,num2+num1)
                elif(i=='-'):
                    operands.insert(0,num2-num1)
                elif(i=='^'):
                    operands.insert(0,num2**num1)
                else:
                    print("Not Valid")
                    a=0
    if(a==1):
        if(len(operands)!=1):
            print("Not valid")
        else:
            print(operands[0])
