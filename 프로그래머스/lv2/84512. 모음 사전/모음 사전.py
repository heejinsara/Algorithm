from itertools import product
def solution(word):
    L=[]
    for i in range(1,6):
        for j in product('AEIOU',repeat=i):
            L.append(''.join(j))
    L.sort()
    return L.index(word)+1