for _ in range(int(input("Enter Number Test Cases you wanna Test: "))):
    s=input("Enter Infix Exxpression: ")
    priority=['/','*','+','-']
    priority.reverse()
    postfix=''
    stack=[]
    for i in range(len(s)):
        if s[i] not in priority:
            postfix+=s[i]
        elif len(stack)>0 and priority.index(s[i])<=priority.index(stack[-1]) :
            while(priority.index(s[i])<=priority.index(stack[-1])and len(stack)>0):
                postfix+=stack[-1]
                stack.pop(-1)
                if len(stack)==0 or priority.index(s[i])>priority.index(stack[-1]):
                    stack+=[s[i]]
                    break
                #print(postfix)
        else:
            stack+=[s[i]]
        #print(stack,postfix)
    while(len(stack)>0):
        postfix+=stack[-1]
        stack.pop(-1)    
    print(postfix)
