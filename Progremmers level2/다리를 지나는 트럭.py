from collections import deque

def solution(bridge_length, weight, truck_weights):
    
    truck = deque(truck_weights)
    passed = deque()
    bridge_weight = 0
    
    count = 0
    while truck or passed:
        
        if passed and passed[0][0] + bridge_length == count:
            done = passed.popleft()
            bridge_weight -= done[1]

        if truck and len(passed) < bridge_length and bridge_weight + truck[0] <= weight:
            on_bridge = truck.popleft()
            passed.append((count, on_bridge))
            bridge_weight += on_bridge
        
        count += 1
        
    return count
