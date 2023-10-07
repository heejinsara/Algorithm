from collections import deque
def solution(prices):
    prices=deque(prices)
    answer=[]
    while prices:
        cnt=0
        temp=prices.popleft()
        for p in prices:
            cnt+=1
            if temp>p:
                break
        answer.append(cnt)
    return answer
            