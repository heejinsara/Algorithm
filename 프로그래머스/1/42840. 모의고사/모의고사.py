def solution(answers):
    L1=[1,2,3,4,5]
    L2=[2,1,2,3,2,4,2,5]
    L3=[3,3,1,1,2,2,4,4,5,5]
    result=[0,0,0]
    for i in range(len(answers)):
        if answers[i]==L1[i%len(L1)]:
            result[0]+=1
        if answers[i]==L2[i%len(L2)]:
            result[1]+=1
        if answers[i]==L3[i%len(L3)]:
            result[2]+=1
    answer=[]
    for i in range(len(result)):
        if result[i]==max(result):
            answer.append(i+1)
    return answer