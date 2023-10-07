import numpy as np
def solution(progresses, speeds):
    answer=[]
    progresses=np.array(progresses)
    speeds=np.array(speeds)
    result=np.ceil((100-progresses)/speeds)
    temp=result[0]
    cnt=1
    for i in result[1:]:
        if i>temp:
            answer.append(cnt)
            cnt=1
            temp=i
        else:
            cnt+=1
    answer.append(cnt)
    return answer