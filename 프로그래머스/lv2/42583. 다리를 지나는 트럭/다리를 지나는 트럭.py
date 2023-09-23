from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge=deque([0]*bridge_length)
    truck_weights=deque(truck_weights)
    temp=0
    time=0
    while truck_weights:
        time+=1
        temp-=bridge.popleft()
        if temp+truck_weights[0]<=weight:
            bridge.append(truck_weights.popleft())
            temp+=bridge[-1]
        else:
            bridge.append(0)
    return time+bridge_length