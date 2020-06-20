for _ in range(int(input("Enter Number 0f Test you wanna Test: "))):
    print("Enter expression over 0 and 1 : ", end=" ")
    lst=list(input())
    initial_state='q0'
    new_state='q1'
    ans_seq=['q0']
    current_state='q0'
    is_valid=1
    for i in range(len(lst)):
        if(lst[i]=='1' and current_state=='q0'):
            current_state='q1'
            ans_seq.append(current_state)
        elif(lst[i]=='1' and current_state=='q1'):
            current_state='q0'
            ans_seq.append(current_state)
        elif(lst[i]=='0'):
            ans_seq.append(current_state)
        else:
            is_valid=0
    if(is_valid):
        if(ans_seq[-1]=='q0'):
            for j in range(len(ans_seq)):
                print(ans_seq[j],end="->")
            print()
            print("Accpeted")
        else:
            print("Not Accpeted")
    else:
        print("Only Binary String!!")
