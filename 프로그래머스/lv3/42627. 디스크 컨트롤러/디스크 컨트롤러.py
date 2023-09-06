from heapq import *
def solution(jobs):
    answer,now,i=0,0,0
    start=-1
    heap=[]
    answer=[]
    while i<len(jobs):
        for job in jobs:
            if start<job[0]<=now:
                heappush(heap,[job[1],job[0]])
        if heap:
            cur=heappop(heap) #걸리는시간, 시점
            start=now
            now+=cur[0]
            answer.append(now-cur[1])
            i+=1
        else:
            now+=1
    return sum(answer)//len(answer)