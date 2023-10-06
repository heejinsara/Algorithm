from collections import defaultdict
def solution(종류):
    D=defaultdict(list)
    for i in 종류:
        D[i[1]].append(i[0])
    answer=1
    for v in D.values():
        answer*=(len(v)+1)
    return answer-1