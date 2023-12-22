import heapq

def solution(scoville, K):
    
    count = 0
  
    heapq.heapify(scoville)
    while scoville[0] < K:    
        count += 1
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        res = first + (second * 2)
        heapq.heappush(scoville, res)
        
        if (len(scoville) == 2) and (scoville[0] + scoville[1]*2) < K: 
            return -1  
    return count
