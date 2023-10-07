from collections import deque
def solution(priorities, location):
    priorities=deque((i,j) for i,j in enumerate(priorities))
    answer=0
    while priorities:
        temp=priorities.popleft()
        if any(temp[1]<p[1] for p in priorities):
            priorities.append(temp)
        else:
            answer+=1
            if temp[0]==location:
                return answer