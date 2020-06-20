def transition(cs, inp):
    if cs=='q0':
        if inp=='a': return 'q1'
        else: return 'q0'
    elif cs=='q1':
        if inp=='a': return 'q1'
        else: return 'q2'
    elif cs=='q2':
        if inp=='a': return 'q1'
        else: return 'q3'
    else:
        if inp=='a': return 'q1'
        else: return 'q0'

for _ in range(int(input("Enter Number of Test Cases You wanna Test: "))):
    exp = input("Enter expression in alphabet over {a, b} : ")
    alphabets = ['a', 'b']
    states = ['q0', 'q1', 'q2', 'q3']
    initial_state = states[0]
    final_state = [states[3]]
    curr_state = initial_state

    for x in exp:
        if x not in alphabets:
            print("Error ! Enter a and b only")
            exit()
    print("Sequence of states:")
    print(curr_state, end = "->")
    for x in exp:
        curr_state = transition(curr_state, x)
        print(curr_state, end = "->")
    print()

    if curr_state in final_state:
        print("Accepted")
    else:
        print("Not Accepted")
