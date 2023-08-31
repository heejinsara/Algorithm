from collections import defaultdict
from itertools import combinations, permutations
def solution(clothes):
    answer=1
    D=defaultdict(list)
    for i in clothes:
        D[i[1]].append(i[0])
    for key in D.keys():
        answer*=(len(D[key])+1)
    return answer-1