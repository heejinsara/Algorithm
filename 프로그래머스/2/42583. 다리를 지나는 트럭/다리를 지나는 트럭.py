from collections import deque
def solution(bridge_length, weight, truck_weights):
    B_weights=deque([0]*bridge_length)
    T_weights=deque(truck_weights)
    time=0
    temp=0
    while T_weights:
        time+=1
        temp-=B_weights.popleft()
        if temp+T_weights[0]<=weight:
            B_weights.append(T_weights.popleft())
            temp+=B_weights[-1]
        else:
            B_weights.append(0)
    #print(time)
    #print(bridge_length)
    return time+bridge_length