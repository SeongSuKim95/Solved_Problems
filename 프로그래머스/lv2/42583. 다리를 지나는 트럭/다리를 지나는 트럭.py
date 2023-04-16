from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    #다리 
    bridge = [0 for _ in range(bridge_length)]
    while(bridge):
        answer+=1
        bridge.pop(0)
        if(truck_weights):
            if(truck_weights[0] + sum(bridge) <= weight):
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return answer