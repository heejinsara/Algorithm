from collections import defaultdict
def solution(clothes):
    answer=1
    D=defaultdict(list)
    for c in clothes:
        D[c[1]].append(c[0])
    for key in D.keys():
        answer*=(len(D[key])+1)
    return answer-1