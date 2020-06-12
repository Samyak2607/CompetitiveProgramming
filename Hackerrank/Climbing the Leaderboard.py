for _ in range(int(input())):
    n = int(input())
    score = list(map(int,input().split()))
    score=list(set(score))
    score.sort(reverse=True)
    m = int(input())
    alice = list(map(int, input().split()))
    dict_score  = {}
    rank=0
    for r in score:
        if r in dict_score:
            continue
        else:
            rank+=1
            dict_score[r]=rank
    score.extend(alice)
    score = list(set(score))
    score.sort(reverse=True)
    count=0
    for r in range(len(score)):
        if score[r] not in dict_score:
            dict_score[score[r]]=r+1-count
            count+=1
    for r in alice:
        print(dict_score[r])
                
