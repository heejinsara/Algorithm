from collections import deque
def solution(priorities, location):
    que=deque((i,j) for i,j in enumerate(priorities))
    answer = 0
    while True:
        cur=que.popleft()
        if any(cur[1]<q[1] for q in que):
            que.append(cur)
        else:
            answer+=1
            if cur[0]==location:
                return answer