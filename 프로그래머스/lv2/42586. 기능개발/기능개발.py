import math
def solution(progresses,speeds):
    result=[]
    answer=[]
    for i in range(len(progresses)):
        result.append(math.ceil((100-progresses[i])/speeds[i]))
    print(result)
    cnt=1
    temp=result[0]
    for j in result[1:]:
        if temp>=j:
            cnt+=1
        else:
            answer.append(cnt)
            temp=j
            cnt=1
    answer.append(cnt)
    return answer