from itertools import permutations
def solution(k, dungeons):
    answer=[]
    for i in permutations(dungeons, len(dungeons)):
        temp=k
        cnt=0
        for j in i:
            if temp>=j[0]:
                temp-=j[1]
                cnt+=1
        answer.append(cnt)
    return max(answer)