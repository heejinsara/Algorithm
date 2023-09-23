from collections import deque
def solution(prices):
    prices=deque(prices)
    answer=[]
    while prices:
        sec=0
        price=prices.popleft()
        for i in prices:
            sec+=1
            if price>i:
                break
        answer.append(sec)
    return answer