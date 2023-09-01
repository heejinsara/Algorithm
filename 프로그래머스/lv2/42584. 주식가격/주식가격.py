from collections import deque
def solution(prices):
    answer=[]
    prices=deque(prices)
    while len(prices)>0:
        sec=0
        price=prices.popleft()
        for i in prices:
            sec+=1
            if price>i:
                break
        answer.append(sec)
    return answer