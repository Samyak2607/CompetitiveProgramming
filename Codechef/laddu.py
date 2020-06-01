for _ in range(int(input())):
    act, origin = map(str, input().split())
    act = int(act)
    laddu=0
    for i in range(act):
        activity = list(map(str, input().split()))
        if len(activity)==2:
            if activity[0]=='CONTEST_WON':
                if int(activity[1])<20:
                    laddu+=(300+20-int(activity[1]))
                else:
                    laddu+=300
            else:
                laddu+=int(activity[1])
        else:
            if activity[0]=='TOP_CONTRIBUTOR':
                laddu+=300
            else:
                laddu+=50
    if origin == 'INDIAN':
        print(laddu//200)
    else:
        print(laddu//400)
