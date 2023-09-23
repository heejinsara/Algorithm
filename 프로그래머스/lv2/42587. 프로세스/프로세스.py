from collections import deque
def solution(priorities, location):
    que=deque((i,j) for i,j in enumerate(priorities))
    answer=0
    while que:
        temp=que.popleft()
        if any(temp[1]<q[1] for q in que):
            que.append(temp)
        else:
            answer+=1
            if temp[0]==location:
                return answer