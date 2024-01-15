def solution(cap, n, deliveries, pickups):
    
    distance = 0
    start = 0
    
    num_deliever = 0
    num_pickups = 0
    
    for i in range(n-1, -1, -1):
        num_deliever += deliveries[i]
        num_pickups += pickups[i]
        
        while num_deliever > 0 or num_pickups > 0:
            num_deliever -= cap
            num_pickups -= cap
            distance += (i+1) * 2
            
    
    
    return distance