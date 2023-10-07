import math
def solution(answers):
    result=[0,0,0]
    answer=[]
    L1=[1,2,3,4,5]
    L2=[2,1,2,3,2,4,2,5]
    L3=[3,3,1,1,2,2,4,4,5,5]
    for i in range(len(answers)):
        if L1[i%len(L1)]==answers[i]:
            result[0]+=1
    for i in range(len(answers)):
        if L2[i%len(L2)]==answers[i]:
            result[1]+=1
    for i in range(len(answers)):
        if L3[i%len(L3)]==answers[i]:
            result[2]+=1
    for i in range(len(result)):
        if result[i]==max(result):
            answer.append(i+1)
    return answer