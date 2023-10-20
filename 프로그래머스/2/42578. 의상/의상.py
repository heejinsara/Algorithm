from collections import defaultdict
def solution(clothes):
    D=defaultdict(list)
    for c in clothes:
        D[c[1]].append(c[0])
    answer=1
    for v in D.values():
        answer*=(len(v)+1)
    return answer-1