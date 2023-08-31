import math
def solution(progresses, speeds):
    result=[]
    answer=[]
    for i,j in zip(progresses, speeds):
        result.append(math.ceil((100-i)/j))
    num=result[0]
    cnt=0
    for k in result:
        if k<=num:
            cnt+=1
        else:
            answer.append(cnt)
            num=k
            cnt=0
            cnt+=1
    answer.append(cnt)
    return answer