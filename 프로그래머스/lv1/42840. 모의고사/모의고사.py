import math
def solution(answers):
    a1=[1, 2, 3, 4, 5]
    a2=[2, 1, 2, 3, 2, 4, 2, 5]
    a3=[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    cnt=[0,0,0]
    answer=[]
    for i in range(len(answers)):
        if a1[i%len(a1)]==answers[i]:
            cnt[0]+=1
        if a2[i%len(a2)]==answers[i]:
            cnt[1]+=1
        if a3[i%len(a3)]==answers[i]:
            cnt[2]+=1
    for j in range(len(cnt)):
        if cnt[j]==max(cnt):
            answer.append(j+1)
    answer.sort()
    return answer