from heapq import *
def solution(scoville,K):
    answer=0
    heapify(scoville)
    while len(scoville)>=2 and scoville[0]<K:
        num1=heappop(scoville)
        num2=heappop(scoville)
        heappush(scoville, num1+2*num2)
        answer+=1
    if scoville[0]<K:
        return -1
    else:
        return answer
            
        