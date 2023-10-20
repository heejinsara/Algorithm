def solution(genres, plays):
    D=dict()
    for idx, g in enumerate(genres):
        if g not in D:
            D[g]=[[idx],plays[idx]]
        else:
            D[g][0].append(idx)
            D[g][1]+=plays[idx]
    D=dict(sorted(D.items(),key=lambda x:x[1][1],reverse=True))
    for g in genres:
        D[g][0].sort(key=lambda x:plays[x], reverse=True)
    answer=[]
    for v in D.values():
        answer.extend(v[0][:2])
    return answer