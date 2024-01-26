import heapq

def solution(jobs):
    
    jobs.sort()
    total = len(jobs)
    q = []
    finish = 0
    now = 0
    while q or jobs:
        
        while jobs and jobs[0][0] <= now:
            start, end = jobs.pop(0)
            heapq.heappush(q, (end, start))
        
        if q:
            end, start = heapq.heappop(q)
            now += end
            finish += now - start
        else:
            now = jobs[0][0]
            
                
    return finish // total
        
# if q문 뒤에 else문이 빠졌을경우 시간초과가 걸림
