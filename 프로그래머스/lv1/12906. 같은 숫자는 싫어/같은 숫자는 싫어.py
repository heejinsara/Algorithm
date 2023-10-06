from collections import deque
def solution(arr):
    arr=deque(arr)
    answer=[]
    answer.append(arr.popleft())
    for i in arr:
        if answer[-1]!=i:
            answer.append(i)
    return answer