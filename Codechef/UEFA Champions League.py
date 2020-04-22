for _ in range(int(input())):
    team={}
    point_list = []
    for i in range(12):
        htn, htg, vs, atg, atn = input().split()
        htg = int(htg)
        atg = int(atg)
        if (htn in team) and (atn in team):
            if htg>atg:
                team[htn]['point']+=3
                team[htn]['gd']+=(htg-atg)
                team[atn]['gd']+=(atg-htg)
            elif htg==atg:
                team[htn]['point']+=1
                team[atn]['point']+=1
            else:
                team[htn]['gd']+=(htg-atg)
                team[atn]['gd']+=(atg-htg)
                team[atn]['point']+=3
        elif htn in team:
            if htg>atg:
                team[htn]['point']+=3
                team[htn]['gd']+=(htg-atg)
                team[atn]={'point':0, 'gd':(atg-htg)}
            elif htg==atg:
                team[htn]['point']+=1
                team[atn]={'point':1, 'gd':(atg-htg)}
            else:
                team[htn]['gd']+=(htg-atg)
                team[atn]={'point':3, 'gd':(atg-htg)}
        elif atn in team:
            if htg>atg:
                team[htn]={'point':3, 'gd':(htg-atg)}
                team[atn]['gd']+=(atg-htg)
            elif htg==atg:
                team[htn]={'point':1, 'gd':(htg-atg)}
                team[atn]['point']+=1
            else:
                team[htn]={'point':0, 'gd':(htg-atg)}
                team[atn]['gd']+=(atg-htg)
                team[atn]['point']+=3
                
        else:
            if htg>atg:
                team[htn]={'point':3, 'gd':(htg-atg)}
                team[atn]={'point':0, 'gd':(atg-htg)}
            elif htg==atg:
                team[htn]={'point':0, 'gd':(htg-atg)}
                team[atn]={'point':0, 'gd':(atg-htg)}
            else:
                team[atn]={'point':3, 'gd':(atg-htg)}
                team[htn]={'point':0, 'gd':(htg-atg)}
    max1_p=-1
    max2_p=-1
    team_sorted = sorted(team, key=lambda x:(team[x]['point'], team[x]['gd']), reverse=True)
    print(team_sorted[0], team_sorted[1])
    
        
        






