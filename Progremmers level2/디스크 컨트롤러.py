import heapq

def solution(jobs):
    
    
    total = len(jobs)
    jobs.sort()
    heap = []
    
    res = 0
    now = 0
    while jobs or heap:
        
    
        
        while jobs and jobs[0][0] <= now:
            respond, request = jobs.pop(0)
            heapq.heappush(heap, (request, respond) )
         
        if heap:
            request, respond = heapq.heappop(heap)
            now += request
            res += now - respond
    
        else:
            now = jobs[0][0]
            start, interval = jobs.pop(0)
            heapq.heappush(heap, (interval, start) )
            
            
            
    return res // total
        
        
