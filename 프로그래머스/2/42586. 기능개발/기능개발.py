import math
def solution(progresses, speeds):
    result=[]
    answer=[]
    for p, s in zip(progresses, speeds):
        result.append(math.ceil((100-p)/s))
    # print(result)
    cnt=1
    temp=result[0]
    for i in result[1:]:
        if temp>=i:
            cnt+=1
        else:
            answer.append(cnt)
            temp=i
            cnt=1
    answer.append(cnt)
    # print(answer)
    return answer